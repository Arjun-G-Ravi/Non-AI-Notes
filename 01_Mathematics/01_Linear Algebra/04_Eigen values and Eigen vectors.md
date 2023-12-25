# 6. Eigenvalues and Eigenvectors

Whenever we do a linear transformation, some vectors just remain in the line in which it spans out. Such vectors are called **eigen vectors**. The amount by which these eigenvectors are stretched are called **eigen values**.

We use this equation to compute the eigen value from eigen vectors for a transformation matrix A.
What this means is that transforming the vector v using A will yield the same result as multiplying the vector with a scalar value λ.
![Alt text](<Screenshot from 2023-12-24 11-48-20.png>)

And, only way two non zero matrices, becoming zero on matmul is if the det(A - λI) is zero. This would mean that the whole transformation squishes the space to a lower dimension.
![Alt text](<Screenshot from 2023-12-24 11-55-37.png>)

## Diagonal Matrices
Diagonal matrices have all basis as eigen vectors, with their eigen values being the diagonal values. This makes them super easy to work with.
![Alt text](<Screenshot from 2023-12-24 12-07-28.png>)

## Use for finding out the eigen vector
When the transformation is 3d rotation, the eigen vector will be the axis of rotation.

![Alt text](<Screenshot from 2023-12-24 11-45-21.png>)

# Characteristic Polynomial
The characteristic polynomial is a concept in linear algebra that is associated with square matrices. Given a square matrix A, the characteristic polynomial is obtained by finding the determinant of the matrix A−λI, where λ is a scalar variable, and I is the identity matrix of the same size as A. The characteristic polynomial is obtained by solving `det(A−λI)= 0`.

The roots of the characteristic equation are the eigen values of the of the matrix. 
