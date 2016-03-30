n = gets.split(" ").map(&:to_i)

if n[0] < n[1] then
  puts "a < b"
elsif n[0] == n[1] then
  puts "a == b"
else
  puts "a > b"
end