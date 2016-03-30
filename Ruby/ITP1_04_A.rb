n = gets.split(" ").map(&:to_i)

d = n[0] / n[1]
r = n[0] % n[1]
f = sprintf("%.5f", n[0] / n[1].to_f)

puts "#{d} #{r} #{f}"