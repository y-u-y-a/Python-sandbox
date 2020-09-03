
import hashlib
import collections

# 目標：blockをhashに変換する

# dictをkeyで揃える(順不同でも同じdictとするため)
def sorted_dict_by_key(unsorted_dict):
    return collections.OrderedDict(
        sorted(unsorted_dict.items(), key=lambda d:d[0]))

# sha256というアルゴリズムでhashを生成する
print(hashlib.sha256("test".encode()).hexdigest())


# 表示用の関数
def pprint(chains):

    for i, chain in enumerate(chains):
        print(f"{'='*25} Chain {i} {'='*25}")
        # key, valueを表示
        for k, v in chain.items():
            if k == "transactions":
                print(k)
                for d in v:
                    print(f"{'-'*40}")
                    for kk, vv in d.items():
                        print(f"{kk:30}{vv}")
            else:
                # k:15は幅揃え
                print(f"{k:15}{v}")

    print(f"{'*'*25}")
