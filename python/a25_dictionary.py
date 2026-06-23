import json
from pathlib import Path


def main():
    # api 전송 보낼때 dictionary
    # yaml, toml, xml, json 의 파이썬 데이터의 형태의 모두 쓰임

    dict_a = dict()
    dict_a = {"a": "aa"}
    print(type(dict_a))

    # 원소 추가
    dict_a["b"] = "bbb"
    print(dict_a)
    print(dict_a["a"], dict_a["b"], dict_a.get("c"))

    print(dict_a)

    dict_a["a"] = "aa"
    dict_a["b"] = "bbb"
    dict_a["c"] = "cccc"
    dict_a["d"] = "ddddd"

    for key, value in dict_a.items():
        print(key, dict_a[key])

    for key, value in dict_a.items():
        print(key, value)

    print(dict_a.keys())
    print(dict_a.values())

    data_dir = Path(__file__).resolve().parent / "data"
    data_dir.mkdir(exist_ok=True)

    with open(data_dir / "dict_a.json", "w", encoding="utf-8") as f:
        json.dump(dict_a, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
