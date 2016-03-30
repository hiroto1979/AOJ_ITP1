n = gets.split(" ").map(&:to_i)

s = 0
for i in n[0]..n[1] do
  if n[2] % i == 0 then
    s += 1
  end
end

puts s