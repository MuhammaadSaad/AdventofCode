import re
"""
board = []
for line in open('input.txt').readlines():
  board.append( line.strip() )
sumCount=0
for row_num in range(len(board)):
   case, games=board[row_num].split(":")
   game1,game2=games.split("|")
   lsg1= game1.strip().split()
   lsg2= game2.strip().split()
   count=0
   for no in lsg1:
      if no in lsg2:
            if count<2:
                count+=1
            else:
                count=2*count
         
         
   #  print(count)
   sumCount+=(count)
print("Part 1:"+str(sumCount))
"""
fileinput=open('input.txt').readlines()
ll = [ l.strip() for l in fileinput ]
s = [ 1 ] * len( ll )
t = 0
for i, l in enumerate( ll ):
    c, p1,p2 = l.replace( ":", "|" ).split( "|" )
    n = len( set( p1.strip().split() ) &
             set( p2.strip().split() ) )
    t += 2 ** ( n - 1 ) if n else 0
    for j in range( 1, min( len( ll ), n + 1 ) ):
        s[ i + j ] += s[ i ]
print( t, sum( s ) )