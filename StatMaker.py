class StatMaker:
    def __init__(self):
        pass

    def compare_stat(self, natasha_stat, marked_stat):
        self.n_org, self.n_per = natasha_stat
        self.m_org, self.m_per = marked_stat
        org_precision, per_precision, total_precision = self.compute_precision()
        org_recall, per_recall, total_recall = self.compute_recall()
        org_f1 = self.compute_f1(org_precision, org_recall)
        per_f1 = self.compute_f1(per_precision, per_recall)
        total_f1 = self.compute_f1(total_precision, total_recall)

        print(f"Statistics:\n  Precision:\n    organisation:{org_precision} person:{per_precision} total:{total_precision}")
        print(f"  Recall:\n    organisation:{org_recall} person:{per_recall} total:{total_recall}")
        print(f"  F1:\n    organisation:{org_f1} person:{per_f1} total:{total_f1}")

    def compute_precision(self):
        org_total_marked = 0
        org_true_marked = 0
        for org in self.n_org:
            org_total_marked += self.n_org[org]
            org_true_marked += min(self.n_org[org], self.m_org[org])

        per_total_marked = 0
        per_true_marked = 0
        for per in self.n_per:
            per_total_marked += self.n_per[per]
            per_true_marked += min(self.n_per[per], self.m_per[per])
        return org_true_marked / org_total_marked, per_true_marked / per_total_marked,\
               (org_true_marked + per_true_marked) / (org_total_marked + per_total_marked)

    def compute_recall(self):
        org_marked = 0
        org_total = 0
        for org in self.m_org:
            org_total += self.m_org[org]
            org_marked += min(self.m_org[org], self.n_org[org])

        per_marked = 0
        per_total = 0
        for per in self.m_per:
            per_total += self.m_per[per]
            per_marked += min(self.m_per[per], self.n_per[per])
        return org_marked / org_total, per_marked / per_total, (org_marked + per_marked) / (org_total + per_total)

    @staticmethod
    def compute_f1(precision, recall):
        return 2 * precision * recall / (precision + recall)
