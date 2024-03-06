# What is the Cyclomatic Complexity of this program
int module1 (int x, int y) {
   while (x!=y){
      if(x>y)
         x=x-y,
      else y=y-x;
      }
   return x;
}

# output may be 1 or 2 or 3 or 4 ??
# Answer  = 3
