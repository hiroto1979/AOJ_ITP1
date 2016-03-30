n = gets.split(" ").map(&:to_i)

S = n[0] * n[1]
syuu = 2 * (n[0] + n[1])

puts "#{S} #{syuu}"