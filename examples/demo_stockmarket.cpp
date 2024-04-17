#include <pybind11/pybind11.h>

namespace py = pybind11;


PYBIND11_MODULE(stockmarket, m) {
  m.doc() = "Stockmarket Example";
  
}
