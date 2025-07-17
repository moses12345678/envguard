import os

def extract_secret_and_database(file_path, outpath):
    output_dir = "data"
    output_path = os.path.join(output_dir, f"{outpath}")

    # Ensure the data folder exists
    os.makedirs(output_dir, exist_ok=True)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found.")

    try:
        with open(file_path, 'r') as f_in, open(output_path, 'w') as f_out:
            in_docstring = False
            inside_databases = False
            db_lines = []
            open_braces = 0

            for line in f_in:
                stripped = line.strip()

                # Skip docstrings
                if stripped.startswith(('"""', "'''")):
                    in_docstring = not in_docstring
                    continue
                if in_docstring or not stripped or stripped.startswith("#"):
                    continue

                # Extract SECRET_KEY
                if stripped.startswith("SECRET_KEY"):
                    f_out.write(stripped + "\n")

                # Capture DATABASES block
                if "DATABASES" in stripped and "=" in stripped:
                    inside_databases = True

                if inside_databases:
                    db_lines.append(line)
                    open_braces += line.count("{")
                    open_braces -= line.count("}")
                    if open_braces == 0:
                        inside_databases = False
                        try:
                            db_text = ''.join(db_lines)
                            local_vars = {}
                            exec(f"result = {db_text.split('=',1)[1].strip()}", {}, local_vars)
                            db_dict = local_vars['result']
                            for key, val in db_dict.get('default', {}).items():
                                f_out.write(f"DATABASE_{key.upper()} = {repr(val)}\n")
                        except Exception as e:
                            f_out.write(f"# Failed to parse DATABASES: {e}\n")
                        db_lines = []
    except Exception as e:
        raise RuntimeError(f"Error reading file: {e}")

    return output_path

if __name__ == "__main__":
    result = extract_secret_and_database("settings.py")
    print(f"✅ Sensitive data saved to: {result}")
