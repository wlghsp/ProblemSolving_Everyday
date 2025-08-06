class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_len = len(name)
        typed_len = len(typed)
        n_idx = t_idx = 0
        while True:
            if n_idx >= name_len or t_idx >= typed_len:
                break

            init_nc = name[n_idx]
            init_tc = typed[t_idx]
            if init_nc != init_tc:
                return False

            ns = init_nc
            while n_idx + 1 < name_len and init_nc == name[n_idx + 1]:
                ns += init_nc
                n_idx += 1


            ts = init_tc
            while t_idx + 1 < typed_len and init_tc == typed[t_idx + 1]:
                ts += init_tc
                t_idx += 1

            if len(ns) > len(ts):
                return False

            n_idx += 1
            t_idx += 1

        if n_idx < name_len or t_idx < typed_len:
            return False

        return True



if __name__ == "__main__":
    sol = Solution()
    print(sol.isLongPressedName("alex", "aaleex")) # true
    print(sol.isLongPressedName("saeed", "ssaaedd")) # false

    print(sol.isLongPressedName("xnhtq", "xhhttqq")) # false
    print(sol.isLongPressedName("alex", "aaleexa")) # false
