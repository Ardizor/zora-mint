# путь до файла с приватниками
private_keys_file = "data/private_keys.txt"

# путь до файла с данными от прокси
proxies_file = "data/proxies.txt"

# путь до файла базы данных
database_file = "data/database.json"

# адреса NFT в сети Zora и количество для бесплатного минта (адрес: количество)
nfts_to_mint = {
    "0x5b9832668e8642a666236b61ed10e77b3b2643dd": 2,
    "0xd0f9af18b93bb3a10240a9aa7650a87929ccbf1b": 1,
    "0x02e78b5ff1dfe31b35ba76d0b1533263613eb9d5": 4,
    "0x8c07329d155ad84718a817e872ff884909f5eff2": 2,
    "0xd1df439912f133b29aaa209d2f25f77cab6a6258": 3,
    "0x626f6ed75b88bcb76024c7ed448c5f140cf3b486": 1,
    "0x4b3cace02cc3ececc5e2927822d0578c5d427ad1": 1,
}

# использование прокси; True - прокси используются, False - не используются
use_proxy = False

# автогенерация базы данных; True - вкл, False - выкл
database_autocreate = True

# минимальный баланс для совершения минта
min_balance = 0.0001

# время между бриджами, [от, до] (выбирается рандомное число)
sleep_time = [10, 30]

# множитель для расчета цен на газ для транзакции
gas_multiplier = 1.5

# максимальная цена газа в Gwei, при которой будет проводиться бридж
gas_threshold = 20

# диапазон времени задержки между проверками текущей цены газа в секундах
gas_delay_range = [10, 15]

# используемая rpc для Zora
zora_rpc = "https://rpc.zora.energy"

# использумая rpc для Ethereum (mainnet)
eth_rpc = "https://rpc.ankr.com/eth"

minter_address = '0x04e2516a2c207e84a1839755675dfd8ef6302f0a'
