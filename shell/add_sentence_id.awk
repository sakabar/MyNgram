BEGIN {
  # FS="\t" #タブ区切りの入力のみを扱う
  s_id = -1
  sub_id = 0
  prev = ""
}

prev == $1 {
  print s_id"\t"sub_id"\t"$0
  sub_id += 1
}

prev != $1 {
  s_id += 1
  sub_id = 0
  print s_id"\t"sub_id"\t"$0
  prev = $1
  sub_id += 1
}



