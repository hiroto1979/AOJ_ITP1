a = gets.to_i
for i in 1..a do
  if i % 3 == 0 || i % 10 == 3 || i.to_s.include?("3")  then
    print " #{i}"
  end
end

puts ""
