import numpy as np

array = np.array(
    [
        [
            ['A','B','C'],['A','B','C']
        ],
        
        [
            ['A','B','C'],['A','B','C']
        ],
        
        [
            ['A','B','C'],['A','B','C']
        ]
    ]
)

#['A','B','C'] 1D

#[['A','B','C'],
#['A','B','C'],
#['A','B','C']] 2D

# [[['A','B','C'],['A','B','C']],
# [['A','B','C'],['A','B','C']],
# [['A','B','C'],['A','B','C']]] 3D


print(array.ndim)#show the dimension of the array
print(array.shape)#shows the (depth,rows,columns)
print(array[0, 1, 1])#indexing