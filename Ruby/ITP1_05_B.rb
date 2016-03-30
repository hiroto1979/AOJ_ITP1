while true
  a = gets.split(" ").map(&:to_i)
  if a[0] == 0 && a[1] == 0 then
    break
  end
  a[1].times{|j|
    print "#"
  }
  puts ""
  (a[0]-2).times{|i|
    print "#"
    (a[1]-2).times{|j|
      print "."
    }
    puts "#"
  }
  a[1].times{|j|
    print "#"
  }
  puts ""
  puts ""
end
