n=gets.to_i
ary = gets.split.map(&:to_i)

minimum = ary.min
maximum = ary.max
s = ary.inject(:+)

puts "#{minimum} #{maximum} #{s}"
