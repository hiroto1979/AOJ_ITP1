n = gets.split(" ").map(&:to_i)

if 0 <= n[2] - n[4] && n[2] + n[4] <= n[0] && 0 <= n[3] - n[4] && n[3] + n[4] <= n[1] then
  puts "Yes"
else
  puts "No"
end
