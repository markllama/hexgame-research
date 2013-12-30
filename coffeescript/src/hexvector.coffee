#
# Hex map location
#
class HexMap if not HexMap?

class HexMap.Vector

    # Constructor signatures
    #   HexMap.Vector()
    #   HexMap.Vector(hx, hy)
    #   HexMap.Vector(hv)

    constructor: (@hx = 0, @hy = 0) ->
      @hz = @hy - @hx

    length: ->
      return Math.max(Math.abs(@hx), Math.abs(@hy), Math.abs(@hz))

    eq: (other) ->
      return @hx == other.hx and @hy == other.hy

    add: (other) ->
      return new HexMap.Vector(@hx + other.hx, @hy + other.hy)
    
    sub: (other) ->
      return new HexMap.Vector(@hx - other.hx, @hy - other.hy)

    mul: (factor) ->
      return new HexMap.Vector(@hx * factor, @hy * factor)
      
    distance: (other) ->
      return other.sub(@).length()
      
    hextant: ->
      ux = 0 ; uy = 0 ; uz = 0

      # get non-normalized non-zero components
      if @hx != 0 then ux = @hx / Math.abs(@hx)
      if @hy != 0 then uy = @hy / Math.abs(@hy)
      if @hz != 0 then uz = @hz / Math.abs(@hz)

      # create a normalized vector
      hunit = new HexMap.Vector(ux, uy)
      for i in [0..6]
        if hunit.equals(HexMap.Vector.UNIT[i]) and hunit.hz is uz
          return i

      for i in [0..6]
        c = HexMap.Vector.HEXTANT[i]
        if ux is c[0] and uy is c[1] and uz is c[2]
          return i

      throw "no hextant"

    rotate: (hextants = 1) ->
      a = [@hy, @hx, -@hz, -@hy, -@hx, @hz, @hy]
      r = hextants % 6
      return new HexMap.Vector(a[r+1], a[r])

    bearing: ->
      # A bearing is the hextant and fraction which precisely defines
      # where a vector points
      h = @hextant()
      n = @rotate(-h)
      f = Math.abs(n.hx) / @length()
      return h + f
      
    angle: (other) ->
      b = @bearing()
      o = other.bearing()

      # normalize o
      if o < b then o += 6
      return o - b
      
# Set the HexVector constants
HexMap.Vector.ORIGIN = new HexMap.Vector()

HexMap.Vector.UNIT = [
  new HexMap.Vector(0, -1),
  new HexMap.Vector(1, 0),
  new HexMap.Vector(1, 1),
  new HexMap.Vector(0, 1),
  new HexMap.Vector(-1, 0),
  new HexMap.Vector(-1, -1)
]
