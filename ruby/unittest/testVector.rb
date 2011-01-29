#!/usr/bin/ruby

require "test/unit"

require "hexgame/vector"

class TestVector < Test::Unit::TestCase
  def testVector
    hv0 = Vector.new(5, 6)
    hv1 = Vector.new(2, -3)

    puts hv0 - hv1

    puts hv0.length

    puts hv0 != hv1
    puts hv0 == hv1
    puts hv0 + hv1
    puts hv0.distance(hv1)

  end
end
