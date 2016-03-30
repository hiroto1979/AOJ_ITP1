while true
  a = gets.split(" ").map(&:to_i)
  if a[0] == 0 && a[1] == 0 then
    break
  end
  a[0].times{|i|
    a[1].times{|j|
      print "#"
    }
    puts ""
  }
  puts ""
end
