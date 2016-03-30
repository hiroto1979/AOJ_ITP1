while true
  n = gets.split(" ").map(&:to_i)
  if n[0] == 0 && n[1] == 0 then
    break
  end
  if n[0] < n[1] then
    puts "#{n[0]} #{n[1]}"
  else
    puts "#{n[1]} #{n[0]}"
  end
end