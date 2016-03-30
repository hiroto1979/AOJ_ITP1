n = gets.split(" ").map(&:to_i)

if n[0] < n[1] && n[1] < n[2] then
  puts "Yes"
else
  puts "No"
end