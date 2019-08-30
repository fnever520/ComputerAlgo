
class Vertex:
    #顶点类
    def __init__(self,vid,outList):
        self.vid = vid#出边
        self.outList = outList#出边指向的顶点id的列表，也可以理解为邻接表
        self.know = False#默认为假
        self.dist = float('inf')#s到该点的距离,默认为无穷大
        self.prev = 0#上一个顶点的id，默认为0
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.vid == other.vid
        else:
            return False
    def __hash__(self):
        return hash(self.vid)

#创建顶点对象1
v1=Vertex(1,[2,3,4,5])
v2=Vertex(2,[3,4,5,6])
v3=Vertex(3,[4,5,6,7])
v4=Vertex(4,[5,6,7,8])
v5=Vertex(5,[6,7,8,9])
v6=Vertex(6,[7,8,9])
v7=Vertex(7,[8,9])
v8=Vertex(8,[9])
v9=Vertex(9,[])
#存储边的权值
edges = dict()
def add_edge(front,back,value):
    edges[(front,back)]=value
add_edge(1,2,1200*50)
add_edge(1,3,1200*50*2)
add_edge(1,4,1200*50*3)
add_edge(1,5,1200*50*4)

add_edge(2,3,1400*50)
add_edge(2,4,1400*50*2)
add_edge(2,5,1400*50*3)
add_edge(2,6,1400*50*4)

add_edge(3,4,1300*50)
add_edge(3,5,1300*50*2)
add_edge(3,6,1300*50*3)
add_edge(3,7,1300*50*4)

add_edge(4,5,1000*50)
add_edge(4,6,1000*50*2)
add_edge(4,7,1000*50*3)
add_edge(4,8,1000*50*4)

add_edge(5,6,1100*50)
add_edge(5,7,1100*50*2)
add_edge(5,8,1100*50*3)
add_edge(5,9,1100*50*4)

add_edge(6,7,1400*50)
add_edge(6,8,1400*50*2)
add_edge(6,9,1400*50*3)

add_edge(7,8,1300*50)
add_edge(7,9,1300*50*2)

add_edge(8,9,1000*50)

#创建一个长度为8的数组，来存储顶点，0索引元素不存
vlist = [False,v1,v2,v3,v4,v5,v6,v7,v8,v9]
#使用set代替优先队列，选择set主要是因为set有方便的remove方法
vset = set([v1,v2,v3,v4,v5,v6,v7,v8,v9])

def get_unknown_min():#此函数则代替优先队列的出队操作
    the_min = 0
    the_index = 0
    j = 0
    for i in range(1,len(vlist)):
        if(vlist[i].know is True):
            continue
        else:
            if(j==0):
                the_min = vlist[i].dist
                the_index = i
            else:
                if(vlist[i].dist < the_min):
                    the_min = vlist[i].dist
                    the_index = i                    
            j += 1
    #此时已经找到了未知的最小的元素是谁
    vset.remove(vlist[the_index])#相当于执行出队操作
    return vlist[the_index]

def main():
    #将v1设为顶点
    v1.dist = 0

    while(len(vset)!=0):
        v = get_unknown_min()
        print(v.vid,v.dist,v.outList)
        v.know = True
        for w in v.outList:#w为索引
            if([w].know is True):
                continue
            if(vlist[w].dist == float('inf')):
                vlist[w].dist = v.dist + edges[(v.vid,w)]
                vlist[w].prev = v.vid
            else:
                if((v.dist + edges[(v.vid,w)])<vlist[w].dist):
                    vlist[w].dist = v.dist + edges[(v.vid,w)]
                    vlist[w].prev = v.vid
                else:#原路径长更小，没有必要更新
                    pass
    output=v.dist+1000*100
    print("output=",output)

                  
main()


