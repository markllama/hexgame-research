#
# Hexgame vector module
#

class Vector
  def initialize(hx, hy)
    @hx = hx
    @hy = hy
  end

  #
  # Accessors
  # 
  def hx 
    @hx
  end

  def hy 
    @hy
  end

  def hz 
    @hy - @hx
  end

  # Implicit
  def to_s
    puts "Vector(#{@hx},#{@hy})"
  end

  #
  # Operators
  # 
  def +(other)
    # assert other is a vector
    Vector.new(@hx + other.hx, @hy + other.hy)
  end

  def -(other)
    # assert other is a Vector
    Vector.new(@hx - other.hx, @hy -other.hy)
  end

  def *(other)
    # assert other is a fixed number
    Vector.new(@hx * other, @hy * other)
  end

  def ==(other)
    @hx == other.hx and @hy == other.hy
  end

  def length
    [@hx.abs, @hy.abs, self.hz.abs].max
  end

  def distance(other)
    (other - self).length
  end
  
  # hextant

  # rotate

  # bearing

  # angle


end

#Vector.ORIGIN = Vector()

#Vector.UNIT = (
#    Vector(0, -1),
#    Vector(1, 0),
#    Vector(1, 1),
#    Vector(0, 1),
#    Vector(-1, 0),
#    Vector(-1, -1)
#    )

#Vector.HEXTANT = (
#    ( 1, -1, -1),
#    ( 1,  1, -1),
#    ( 1,  1,  1),
#    (-1,  1,  1),
#    (-1, -1,  1),
#    (-1, -1, -1)
#    )
