from pydantic import BaseSettings
from src.core.constants import Environments


class AuthConfig(BaseSettings):
    JWT_ALG: str = "HS256"
    JWT_SECRET: str = "JWT_SECRET"
    JWT_EXP: int = 5  # minutes
    REFRESH_TOKEN_KEY: str = "refreshToken"
    REFRESH_TOKEN_EXP: int = 60 * 60 * 24 * 21  # 21 days

    SECURE_COOKIES: bool = True


class ExecutorConfig(BaseSettings):
    FIREBLOCK_SECRET_KEY: str = '''-----BEGIN PRIVATE KEY-----
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
5c13/SXWVoOVa4BWFRGDZa6eU/vYow==
-----END PRIVATE KEY-----'''
    FIREBLOCK_API_KEY: str = "c9bf54cf-d5f6-4240-a762-4020e888c3fb"
    FIREBLOCK_API_URL: str = "https://sandbox-api.fireblocks.io"

    WITHDRAWAL_POOL_ACCOUNT_ID: int = 62

    UPDATE_WITHDRAW_CALLBACK_URL: str = "https://<update-withdraw-callback>"

    enviroment: str = Environments.STAGING

    mapping_crypto_code = {
        "ETH": "ETH_TEST5"
    }
    PUBLIC_KEYS = {
        '0': '''-----BEGIN PUBLIC KEY-----
MEkwEwYHKoZIzj0CAQYIKoZIzj0DAQEDMgAEGExtWnDQ4y9MEnSwGiUuSsBt9MiJ
FDtoIf53b3OfIpRrxxM0EobFf5CEU52hv+mi
-----END PUBLIC KEY-----''',
        '1': '''-----BEGIN PUBLIC KEY-----
MEkwEwYHKoZIzj0CAQYIKoZIzj0DAQEDMgAEAL+Euc8ZzQLVuQHSALud3yX1rCj+
F24mJQf6qr7P+eo2K7qlj8pQo/Qd/+B8jwsl
-----END PUBLIC KEY-----''',
        '2': '''-----BEGIN PUBLIC KEY-----
MEkwEwYHKoZIzj0CAQYIKoZIzj0DAQEDMgAEtroXwDzr57XFLM3q8rMaSLB5Hc/D
RMIzE6tCTdghcIXCvaMDy2wkMKyvG2WXdV+9
-----END PUBLIC KEY-----''',
        '3': '''-----BEGIN PUBLIC KEY-----
MEkwEwYHKoZIzj0CAQYIKoZIzj0DAQEDMgAEVt/G49RdzxcCwJ5ebVFtiM+OFo9B
zi6LeK2IjazF5QKlkWNGjeWInCAfmvug7b2P
-----END PUBLIC KEY-----'''
    }

    LIMIT_AMOUNT = [
        {
            'limit': (0, 1_000_001),
            'node': 3,
            'admin': False
        },
        {
            'limit': (1_000_001, 10_000_001),
            'node': 4,
            'admin': False
        },
        {
            'limit': (10_000_001, 100_000_001),
            'node': 5,
            'admin': False
        },
        {
            'limit': 100_000_001,
            'node': 5,
            'admin': True
        }
    ]

executor_config = ExecutorConfig()
