#!/usr/bin/ruby

require "test/unit"

require "hexgame/vector"

class TestVector < Test::Unit::TestCase

  def testConstants

  end

  def testConstructor

    # two arguments
    hv2 = HexMap::Vector.new(2, -3)
    assert_equal(hv2.hx, 2)
    assert_equal(hv2.hy, -3)

    # one argument
    hv1 = HexMap::Vector.new(hv2)
    assert_equal(hv1.hx, 2)
    assert_equal(hv1.hy, -3)

    # no arguments
    hv0 = HexMap::Vector.new
    assert_equal(hv0.hx, 0)
    assert_equal(hv0.hy, 0)

    # three arguments:
    assert_raise (ArgumentError) { hv3 = HexMap::Vector.new(1, 2, 3) }

  end
  
  def testAccessors
    hv0 = HexMap::Vector.ORIGIN

    assert_equal(0, hv0.hx)
    assert_equal(0, hv0.hy)
    assert_equal(0, hv0.hz)

    hv1 = HexMap::Vector.new(1, -1)
    assert_equal(1, hv1.hx)
    assert_equal(-1, hv1.hy)
    assert_equal(-2, hv1.hz)
  end

  def testString
    hv0 = HexMap::Vector.new(5, -6)
    hv0str = hv0.to_s
    assert_equal("Vector(5,-6)", hv0str)
  end

  def testAdd
    hv0 = HexMap::Vector.new(5, -6)
    hv1 = HexMap::Vector.new(-2, 14)

    hv2 = hv0 + hv1

    assert_equal(3, hv2.hx)
    assert_equal(8, hv2.hy)
    assert_equal(5, hv2.hz)
  end

  def testSubtract
    hv0 = HexMap::Vector.new(5, -6)
    hv1 = HexMap::Vector.new(-2, 14)

    hv2 = hv0 - hv1

    assert_equal(7, hv2.hx)
    assert_equal(-20, hv2.hy)
    assert_equal(-27, hv2.hz)
  end

  def testMultiply
    hv0 = HexMap::Vector.new(5, -6)
    hv1 = hv0 * 4

    assert_equal(20, hv1.hx)
    assert_equal(-24, hv1.hy)
    assert_equal(-44, hv1.hz)
  end

  def testEqual
    hv0 = HexMap::Vector.new(5, -6)
    hv1 = HexMap::Vector.new(5, -6)
    hv2 = HexMap::Vector.new(4, 3)

    assert_equal(hv0, hv1)
    assert_not_equal(hv0, hv2)
  end

  def testLength
    assert_equal(0, HexMap::Vector.ORIGIN.length)
    for i in 0..5
      assert_equal(1, HexMap::Vector.UNIT[i].length)
    end

    hv0 = HexMap::Vector.new(4, 9)
    assert_equal(9, hv0.length)

    hv1 = HexMap::Vector.new(-5, -10)
    assert_equal(10, hv1.length)
  end

  def testDistance
    assert_equal(0, HexMap::Vector.ORIGIN.distance(HexMap::Vector.ORIGIN))
   
    for i in 0..5
      assert_equal(0, HexMap::Vector.UNIT[i].distance(HexMap::Vector.UNIT[i]))      
    end

    for i in 0..5
      assert_equal(1, HexMap::Vector.UNIT[i].distance(HexMap::Vector.ORIGIN))
      assert_equal(2, HexMap::Vector.UNIT[i].distance(HexMap::Vector.UNIT[(i + 3) % 6]))
      assert_equal(1, HexMap::Vector.ORIGIN.distance(HexMap::Vector.UNIT[i]))
    end

    hv0 = HexMap::Vector.new(4, 6)
    hv1 = HexMap::Vector.new(-10, -2)

    assert_equal(14, hv0.distance(hv1))
    assert_equal(14, hv1.distance(hv0))
  end

  def testHextant

    # test on-axis

    # test off-axis
  end

  def testRotate
    
    hv0 = HexMap::Vector.UNIT[0]
    for i in 0..5
      assert_equal(HexMap::Vector.UNIT[i], hv0.rotate(i))
    end

    for i in -6..-1
      assert_equal(HexMap::Vector.UNIT[i+6], hv0.rotate(i))
    end

    hv0 = HexMap::Vector.new(0, 5)
  end

  def testBearing
  end

  def testAngle
  end

end
