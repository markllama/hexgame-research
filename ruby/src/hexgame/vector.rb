#
# Hexgame vector module
#

module HexMap
  class Vector
    
    attr_reader :hx, :hy, :hz
  
    def initialize(*args)
      if args.length == 2
        # TODO: check that both args are Fixnum
        @hx, @hy = args
      elsif args.length == 1
        # TODO: check that the arg is a Vector
        other = args[0]
        @hx, @hy = other.hx, other.hy
      elsif args.length == 0
        @hx, @hy = 0, 0
      else
        raise ArgumentError, "Vector requires 0-2 arguments: #{args.length} given"
      end
      @hz = @hy - @hx
    end

    # Implicit
    def to_s
      "Vector(#{@hx},#{@hy})"
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
      Vector.new(@hx - other.hx, @hy - other.hy)
    end

    def *(other)
      # assert other is a fixed number
      Vector.new(@hx * other, @hy * other)
    end

    def ==(other)
      @hx == other.hx and @hy == other.hy
    end

    def length
      [@hx.abs, @hy.abs, @hz.abs].max
    end

    def distance(other)
      (other - self).length
    end
  
    # hextant
    def hextant
      ux, uy, uz = 0, 0, 0

      # get non-normalized non-zero components
      if @hx != 0: ux = @hx / @hx.abs end
      if @hy != 0: uy = @hy / @hy.abs end
      if @hz != 0: uz = @hz / @hz.abs end

      # Create normalized vector
      hunit = Vector.new(ux, uy)
      for i in 0..5 do
        if hunit == @UNIT[i] and hunit.hz == uz
          return i
        end
      end

      for i in 0..5 do
        c = @@HEXTANT[i]
        if ux == c[0] and uy == c[1] and uz == c[2]
          return i
        end
      end

      # raise an exception: no hextant

    end

    # rotate
    def rotate(hextants=1)
      a = [@hy, @hx, -@hz, -@hy, -@hx, @hz, @hy]
      r = hextants % 6
      Vector.new(a[r+1], a[r])
    end
  
    # bearing
    def bearing
      h = self.hextant
      n = self.rotate(-h)
      f = float(n.hx.abs) / self.length
      h + f
    end

    # angle
    def angle(other)
      b = self.bearing
      o = other.bearing

      if o < b: o += 6 end
      o - b
    end

    @@ORIGIN = Vector.new(0,0)

    def self.ORIGIN
      return @@ORIGIN
    end

    @@UNIT = [
              Vector.new(0, -1),
              Vector.new(1, 0),
              Vector.new(1, 1),
              Vector.new(0, 1),
              Vector.new(-1, 0),
              Vector.new(-1, -1)
             ]

    def self.UNIT
      return @@UNIT
    end

    @@HEXTANT = [               
                 [ 1, -1, -1],
                 [ 1,  1, -1],
                 [ 1,  1,  1],
                 [-1,  1,  1],
                 [-1, -1,  1],
                 [-1, -1, -1]
                ]

  end
end

