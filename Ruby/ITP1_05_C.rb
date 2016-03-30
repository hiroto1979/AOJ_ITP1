while true
  a = gets.split(" ").map(&:to_i)
  if a[0] == 0 && a[1] == 0 then
    break
  end
  1.upto(a[0]){|i|
    1.upto(a[1]){|j|
      if (i + j) % 2 == 0 then
        print "#"
      else
        print "."
      end
    }
    puts ""
  }
  puts ""
end
