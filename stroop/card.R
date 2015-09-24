ncol <- 4
nrow <- 8

share <- function (x,y) { any(x - y == 0) }

a <- matrix(rep(0,ncol*nrow),ncol=4)

try.again = 1

while (try.again == 1)
  {

oldcol <- rep(99, ncol)
for (i in 1:nrow) {
  x <- sample(1:ncol)
  if (i > 1) {
    while (share(x, a[i-1, ])) 
      { x <- sample(1:ncol) }
  }
  a[i,] <- x
}

try.again = 0
for (i in 1:ncol) {
  if (any( table(a[,i]) == 0 )) { try.again=1; break }
}

}

a

