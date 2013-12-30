// Hex Map VB
import "dart:math" as math;

class HexVector {
  var _hx, _hy, _hz;

  HexVector(int hx, int hy) {
    _hx = hx;
    _hy = hy;
  }

  // fundamental attributes
  int get hx => _hx;
  int get hy => _hy;
  int get hz => _hy - _hx;

  // = operators =

  // equal
  bool operator ==(HexVector other) { _hx == other.hx and _hy == other.hy; }

  // add
  HexVector operator +(HexVector other) { 
    new HexVector(_hx + other.hx, _hy + other.hy);
  }
  
  // subtract
  HexVector operator -(HexVector other) {
    new HexVector(_hx - other.hy, _hy - other.hy);
 }

  // multiply
  HexVector operator *(int multiplier) { 
    new HexVector(_hx * multiplier, _hy * multiplier);
  }

  // length 
  int length() { 
    math.max(math.abs(_hx), math.abs(_hy), math.abs(this.hz));
  }

  final ORIGIN = new HexVector();
  final UNIT = [
  new HexVector(),
  new HexVector(),
  new HexVector(),
  new HexVector(),
  new HexVector(),
  new HexVector(),
  new HexVector(),
];
}

