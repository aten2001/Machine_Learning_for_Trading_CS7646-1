"""                          
A simple wrapper for linear regression.  (c) 2015 Tucker Balch                          
                          
Copyright 2018, Georgia Institute of Technology (Georgia Tech)                          
Atlanta, Georgia 30332                          
All Rights Reserved                          
                          
Template code for CS 4646/7646                          
                          
Georgia Tech asserts copyright ownership of this template and all derivative                          
works, including solutions to the projects assigned in this course. Students                          
and other users of this template code are advised not to share it with others                          
or to make it available on publicly viewable websites including repositories                          
such as github and gitlab.  This copyright statement should not be removed                          
or edited.                          
                          
We do grant permission to share solutions privately with non-students such                          
as potential employers. However, sharing with other current or future                          
students of CS 7646 is prohibited and subject to being investigated as a                          
GT honor code violation.                          
                          
-----do not edit anything above this line---                          
"""                          
                          
import numpy as np 
import random
                          
class DTLearner(object):                          
                          
    def __init__(self, leaf_size = 1, verbose = False):
        self.leaf_size=leaf_size 
                          
    def author(self):                          
        return 'tpasumarthi3' # replace tb34 with your Georgia Tech username                          
                          
    def addEvidence(self,dataX,dataY):                          
        """                          
        @summary: Add training data to learner                          
        @param dataX: X values of data to add                          
        @param dataY: the Y training values                          
        """                          
                          
        # slap on 1s column so linear regression finds a constant term                          
        newdataX = np.ones([dataX.shape[0],dataX.shape[1]+1])                          
        newdataX[:,0:dataX.shape[1]]=dataX
        newdataX[:,-1]=dataY
        self.tree= buildTree(newdataX)
    
    def buildTree(data):
        if(data.shape[0]==1):
            return np.array([[-1,data[0][-1],-1,-1]])
        elif(np.all(data[:,-1])==data[0][-1]):
            return np.array([[-1,data[0][-1],-1,-1]])
        else:
            best_i= random.randint(0,data.shape[1]-2)
            splitVal= np.median(data[:,best_i],axis=0)
            lefttree=self.build_tree(data[data[:,i]<=SplitVal])
            righttree=self.build_tree(data[data[:,i]>SplitVal])
            
            return np.vstack(np.vstack(root,leftree),righttree)

                          
    def query(self,points):                          
        """                          
        @summary: Estimate a set of test points given the model we built.                          
        @param points: should be a numpy array with each row corresponding to a specific query.                          
        @returns the estimated values according to the saved model.                          
        """
        ret_vals[]
        for point in points:
            result= query_tree(points,0)
            ret_vals.append(result)
        return ret_vals
    
    def query_tree(self, point, node):
        index= int(self.tree[node,0])
        splitVal= self.tree[node,1]
        
        if(index==-1):
            return splitVal
        elif (point[index]<=splitVal):
            left= self.tree[node,2]
            new_node=int(node+left)
            return querry_tree(point,new_node)
        else:
            right= self.tree[node,2]
            new_node=int(node+right)
            return querry_tree(point,new_node)
                          
if __name__=="__main__":                          
    print("the secret clue is 'zzyzx'")                          
