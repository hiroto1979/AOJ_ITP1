while true
  a,op,b = gets.split.map(&:to_s)

  case op
    when "?" then
      break
    when "+" then
      puts a.to_i + b.to_i
    when "-" then
      puts a.to_i - b.to_i
    when "*" then
      puts a.to_i * b.to_i
    when "/" then
      puts a.to_i / b.to_i
    else
      break
  end
end