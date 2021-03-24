function rowSumOddNumbers(n) {
  i = 0;
  a = (n*n)-(n-1);
  c = a;
  
  for (i=0; i < n-1; i++){
    a = a+2;
    c = c+a;
  }
  return(c);
}
