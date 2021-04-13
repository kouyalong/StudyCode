# -*- coding: utf-8 -*-


"""
缓慢的爬虫
Description

C 公司开发了一款号称是学院路最强漏洞扫描器的工具，并推荐给了公司负责安全服务的 Alice 同学试用。Alice 同学试用过后开始了疯狂吐槽，其中吐槽得最厉害的是扫描器的爬虫很不给力，目标网站的很多页面都扫不出来。然而扫描器的开发同学 Bob 表示并不相信，和 Alice 一起认真研究之后，发现原来是目标网站有些页面响应很慢，超过了 Alice 同学给扫描器配置的超时阈值，导致很多页面没有扫描出来，果然不是扫描器爬虫的问题(==)。 Alice 表示接受，但是她也希望扫描过程能够尽快完成，所以她希望知道自己应该把超时阈值最小配置为多少可能保证 P\%P% 页面能被发现 (一个页面只有响应完成才能算被发现)。


Input
第 1 行输入 1 个整数 TT (1 \le T \le 101≤T≤10)，表示一共有 T 组数据；

对于每一组数据:

第 1 行输入 2 个整数 NN, PP (1 \le N \le 10000001≤N≤1000000)，表示目标网站有 NN 个页面，编号从 1 到 NN，PP 表示希望 P\%P% 的页面被发现 (0 \le P \le 1000≤P≤100)；
接下来一行输入 NN 个整数，第 ii 个整数表示页面 ii 响应需要的时间 t_{i}t
i
​
  (0 &lt; t_{i} \le 100000000<t
i
​
 ≤10000000)；
接下来输入 NN 行，第 ii 行用于表示页面 ii 有哪些页面的链接，每行先输入一个整数 C_{i}C
i
​
  (0 \le C_{i} &lt; N0≤C
i
​
 <N)，表示页面 i 有C_{i}C
i
​
  个链接，该行接下来是C_{i}C
i
​
 个整数，表示页面 ii 的中具体有到哪些页面的链接。
PS: 爬虫总是从页面 1 的链接开始爬取，总链接数不超过 1000000；

PPS: 输入保证合法；

PPPS: 当超时阈值为 t 时，如果一个页面加载时间刚好需要 tt，该页面也属于无法打开的页面。


Output
针对每组输入，如果某个配置能达到目标，则输出 Alice 能配置的最小超时时间(整数，必须 \ge 0≥0)，如果无论如何配置都达不到目标，则输出 -1 。


example:
6
1 100
100
0
5 100
100 200 300 400 500
1 2
1 3
1 4
1 5
0
4 100
100 200 300 400
3 2 3 4
0
0
0
5 100
1 500 1 1 1
1 2
1 3
1 4
1 5
0
5 100
1 1 1 1 1
1 2
1 3
0
1 5
0
5 80
100 200 300 400 500
1 2
1 3
1 4
1 5
0

answer:
101
501
401
501
-1
401

"""

data_example = [
    {
        "percent": "",
        "timeout": [],
        "relate": {}
    }
]


data = []

lines = input().split("\n")
pro_sum = int(lines[0])
index = 1
for i in range(pro_sum):
    n, p = [int(_n) for _n in lines[index].split(" ")]
    ppp = {
        "percent": p,
        "timeout": [int(_n) for _n in lines[index+1].split(" ")],
        "relate": {}
    }
    relate = dict()
    default_n = index + 2
    for j in range(default_n, default_n+n):
        nums = [int(o) for o in lines[j].split(" ")]
        if nums[0] == 0:
            pass
        relate.setdefault(j-default_n, []).append()
    index = index + 2 + n
    data.append()


def to_int(line: str):
    return [int(_n) for _n in line.split(" ")]




