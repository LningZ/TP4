class Noeud:

    def __init__(self,nom,enfants = None):
        self.nom = nom
        self.enfants = enfants if enfants is not None else [] # 默认enfants是None
        

    def ajouter_enfants(self,noeud):
        self.enfants.append(noeud)
    
    
    def afficher(self):
        if not self.enfants: # 如果一个节点没有子节点，它可能是一个常数、变量或者没有参数的函数（如 x 或 3）。在这种情况下，方法直接返回节点的名称 (self.nom)，因为没有更多的子表达式需要处理。
            return self.nom
        else:
            result = ""
            first = True # 用于跟踪是否是第一个子节点，以便正确地添加逗号分隔符,因为第一个不需要逗号
            for enfants in self.enfants:
                if not first:
                    result += ", " # 在除第一个子节点外的节点前添加逗号和空格
                result += enfants.afficher()
                first = False  # 更新first标志，表示已处理过至少一个子节点
            result = self.nom + "(" + result + ")"
            return result
       



class Arbre:
    def __init__(self,racine):
        self.racine = racine

    def afficher(self):
        return self.racine.afficher()