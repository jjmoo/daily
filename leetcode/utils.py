import time

class Benchmark():
    """Benchmark programs."""
    def __init__(self, prefix=None):
        self.prefix = prefix + ' ' if prefix else ''

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, *args):
        print('%stime: %.4f sec' % (self.prefix, time.time() - self.start))


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        sb = str(self.val)
        p = self.next
        while p:
            sb += f'->{p.val}'
            p = p.next
        return sb

    @staticmethod
    def create_node(lists):
        p = dummy = ListNode(0)
        for x in lists:
            p.next = ListNode(x)
            p = p.next
        print('create:', dummy.next)
        return dummy.next

    @staticmethod
    def create_lists(lists):
        return [ListNode.create_node(l) for l in lists]
