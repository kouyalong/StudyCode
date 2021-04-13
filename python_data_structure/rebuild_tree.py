# -*- coding: utf-8 -*-


"""
第九题：

create table bank (
	`id` INT (11) NOT NULL AUTO_INCREMENT,
	`rank` TINYINT(4) not null default 0 comment "行类型：0:分行 1：总行",
	`head_bank_id` INT(11) not null default 0 comment "分行关联总行id",
	`address` varchar(255) not null default "" comment "地址",
	`name` varchar(64) not null default "" comment "名称",
  `created_time` datetime NOT NULL,
  `updated_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_bank_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 comment "银行信息表";


create table customer (
	`id` INT (11) NOT NULL AUTO_INCREMENT,
	`user_name` varchar(64) not null default "" comment "用户名称",
	`phone` varchar(20) not null default "" comment "用户手机",
	`open_account_bank_id` INT(11) not null default 0 comment "开户行id",
  `created_time` datetime NOT NULL,
  `updated_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_customer_open_account_bank_id` (`open_account_bank_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 comment "顾客信息表";


create table bank_order (
	`id` INT (11) NOT NULL AUTO_INCREMENT,
	`type` TINYINT(4) not null comment "业务类型：0:存款 1：贷款",
	`bank_id` INT(11) not null comment "办理业务行id",
	`customer_id` INT(11) not null comment "办理业务用户id",
  `created_time` datetime NOT NULL,
  `updated_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_order_bank_id` (`bank_id`),
  KEY `idx_order_customer_id` (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 comment "顾客业务表";


"""


"""第十题"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def re_build(self, post, tin):
        if len(post) == 0 or len(tin) == 0:
            return None

        root = TreeNode(post[-1])
        i = tin.index(post[-1])

        root.left = self.re_build(post[0: i], tin[0: i])
        root.right = self.re_build(post[i: -1], tin[i + 1:])
        return root

    def traverse_order(self, root):
        if not root:
            return []
        result = list()
        nodes = [root]
        while nodes:
            node = nodes.pop(0)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
            result.append(node.val)
        return result


s = Solution()
po = [2, 3, 1, 5, 7, 6, 4]
io = [1, 2, 3, 4, 5, 6, 7]

print(s.traverse_order(s.re_build(po, io)))
