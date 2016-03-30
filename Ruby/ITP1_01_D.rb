S = gets.to_i
# n = x.split(" ").map(&:to_i)

s = S % 60;
M = (S - s) / 60;
m = M % 60;
h = (M - m) / 60;

puts "#{h}:#{m}:#{s}"
