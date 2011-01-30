#!/usr/bin/ruby

require "test/unit"

require "hexgame/vector"

class TestVector < Test::Unit::TestCase

  def testConstants

  end

  def testConstructor

    # two arguments
    hv2 = Vector.new(2, -3)
    assert_equal(hv2.hx, 2)
    assert_equal(hv2.hy, -3)

    # one argument
    hv1 = Vector.new(hv2)
    assert_equal(hv1.hx, 2)
    assert_equal(hv1.hy, -3)

    # no arguments
    hv0 = Vector.new
    assert_equal(hv0.hx, 0)
    assert_equal(hv0.hy, 0)

    # three arguments:
    assert_raise (ArgumentError) { hv3 = Vector.new(1, 2, 3) }

  end
  
  def testAccessors
    hv0 = Vector.ORIGIN

    assert_equal(0, hv0.hx)
    assert_equal(0, hv0.hy)
    assert_equal(0, hv0.hz)

    hv1 = Vector.new(1, -1)
    assert_equal(1, hv1.hx)
    assert_equal(-1, hv1.hy)
    assert_equal(-2, hv1.hz)
  end

  def testString
    hv0 = Vector.new(5, -6)
    hv0str = hv0.to_s
    assert_equal("Vector(5,-6)", hv0str)
  end

  def testAdd
    hv0 = Vector.new(5, -6)
    hv1 = Vector.new(-2, 14)

    hv2 = hv0 + hv1

    assert_equal(3, hv2.hx)
    assert_equal(8, hv2.hy)
    assert_equal(5, hv2.hz)
  end

  def testSubtract
    hv0 = Vector.new(5, -6)
    hv1 = Vector.new(-2, 14)

    hv2 = hv0 - hv1

    assert_equal(7, hv2.hx)
    assert_equal(-20, hv2.hy)
    assert_equal(-27, hv2.hz)
  end

  def testMultiply
    hv0 = Vector.new(5, -6)
    hv1 = hv0 * 4

    assert_equal(20, hv1.hx)
    assert_equal(-24, hv1.hy)
    assert_equal(-44, hv1.hz)
  end

end
