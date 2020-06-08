Set c(*) "country names"
    / Colombia
      Brazil
      Mexico
      Argentina /;

Set cty(*) "large cities"
    / "Sao Paolo"
      Guadalajara
      "Mexico City"
      Bogota
      "Buenos Aires"
      Lima /;

Parameter  
    dd(c) "distribution of demand"
                         /  Mexico   55,
                            Brazil   15 /;

Table pop(c,cty) "population of cities in countries"
                   "Mexico City" "Buenos Aires" Guadalajara "Sao Paolo"
    Mexico          12                          2
    Argentina                     3                          1
    Brazil                                                   5
