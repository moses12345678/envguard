# envguard

**envguard** is a Python tool to extract and encrypt sensitive environment variables from Django `settings.py` or `.env` files using AES-256 encryption. It helps secure your secret keys, database credentials, and other sensitive values — without disrupting your workflow.

## 🔐 Features

- Extracts `SECRET_KEY` and `DATABASES` config from Django settings
- Outputs to `.env` format
- Encrypts only the values using AES-256 (CBC mode + PKCS7)
- Generates secure key and IV and saves them to a file
- CLI-ready: coming soon with `argparse`
- MIT licensed and open for contributions

## 📄 Example

### Original `.env`
```
SECRET_KEY = "django-insecurasdfasfe-*ysdfsl=ksdlkjlskdjfl1ffvr4o5)#q*s(m@uv_7$u#b%4(biypf=9s695m17nl*b"
DATABASE_ENGINE = 'django.db.backends.psysql'
DATABASE_NAME = 'jdjakdjkanxa'
DATABASE_USER = 'mosdfssdfklkfes'
DATABASE_PASSWORD = 'oisjdfoijlk22343'
DATABASE_HOST = '34.223.27.252'
DATABASE_PORT = '3306'
DATABASE_OPTIONS = {'charset': 'utf8mb4', 'use_unicode': True}
```

### Encrypted Output
```
SECRET_KEY = ENC(f645f3b7d223a4fa86d77c70...)
DATABASE_ENGINE = ENC(19a2c476dd4ed89171...)
DATABASE_NAME = ENC(62c9f513c51a3880...)
DATABASE_USER = ENC(7ffb38cd9fa2a2e13e2...)
DATABASE_PASSWORD = ENC(9870a7fbb2f5ca3c5a7...)
DATABASE_HOST = ENC(a2e3675e98e841cbfe7...)
DATABASE_PORT = ENC(5c934a2a5fd374bc9b...)
DATABASE_OPTIONS = ENC(56c899f0dc2c3e2bfc9...)
```

## 🚀 Quickstart

1. Extract sensitive values:
```bash
python extractor.py settings.py
```

2. Generate key and IV:
```bash
python key_manager.py
```

3. Encrypt:
```bash
python encryptor.py
```

4. Decrypt:
```bash
python decryptor.py
```

## 🎯 Next Goals

- [x] AES encryption
- [x] Clean `.env` extraction
- [ ] Add `argparse` CLI support
- [ ] Publish to PyPI as `envguard`
- [ ] Add auto key rotation

## 🤝 Contribute

This project is open under the MIT License.

Take your time, understand the flow, and write the code yourself. The goal is to learn deeply, not copy blindly.

## License

MIT
