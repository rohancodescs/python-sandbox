def is_present(lst,x):
  lst2 = [y for y in lst if y == x]
  print(list(lst2))

def main():
    lst = [1,2,3,4,5,6,7,8,9,10]
    is_present(lst, 4)
if __name__ == "__main__":
    main()
