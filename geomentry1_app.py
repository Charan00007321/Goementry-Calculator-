import streamlit as st
import math

# ---------- 2D SHAPES ----------

def triangle_perimeter(a, b, c):
    return a + b + c

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def square_perimeter(side):
    return 4 * side

def square_area(side):
    return side ** 2

def rectangle_perimeter(l, b):
    return 2 * (l + b)

def rectangle_area(l, b):
    return l * b

def circle_perimeter(r):
    return 2 * math.pi * r

def circle_area(r):
    return math.pi * r ** 2


# ---------- 3D SHAPES ----------

def cone_tsa(r, l):
    return math.pi * r * (r + l)

def cone_vol(r, h):
    return (1/3) * math.pi * r**2 * h

def cube_tsa(s):
    return 6 * s**2

def cube_vol(s):
    return s**3

def cuboid_tsa(l, b, h):
    return 2 * (l*b + b*h + h*l)

def cuboid_vol(l, b, h):
    return l * b * h

def cylinder_tsa(r, h):
    return 2 * math.pi * r * (r + h)

def cylinder_vol(r, h):
    return math.pi * r**2 * h


# ---------- UI ----------
st.title("Geometry Calculator")

st.header("2D Shapes")

# -------- Triangle --------
st.subheader("Triangle")

a = st.number_input("Side 1", min_value=0.0, key="t1")
b = st.number_input("Side 2", min_value=0.0, key="t2")
c = st.number_input("Side 3", min_value=0.0, key="t3")

col1, col2 = st.columns(2)

with col1:
    st.metric("Perimeter", triangle_perimeter(a, b, c))

with col2:
    if a + b > c and a + c > b and b + c > a:
        st.metric("Area", triangle_area(a, b, c))
    else:
        st.metric("Area", "Invalid triangle")


st.divider()

# -------- Rectangle --------
st.subheader("Rectangle")

l = st.number_input("Length", min_value=0.0, key="r1")
b = st.number_input("Breadth", min_value=0.0, key="r2")

col1, col2 = st.columns(2)

with col1:
    st.metric("Perimeter", rectangle_perimeter(l, b))

with col2:
    st.metric("Area", rectangle_area(l, b))


st.divider()

# -------- Circle --------
st.subheader("Circle")

r = st.number_input("Radius", min_value=0.0, key="c1")

col1, col2 = st.columns(2)

with col1:
    st.metric("Circumference", circle_perimeter(r))

with col2:
    st.metric("Area", circle_area(r))


st.divider()

# -------- Square --------
st.subheader("Square")

s = st.number_input("Side", min_value=0.0, key="s1")

col1, col2 = st.columns(2)

with col1:
    st.metric("Perimeter", square_perimeter(s))

with col2:
    st.metric("Area", square_area(s))


# ================= 3D SHAPES =================

st.divider()
st.header("3D Shapes")

# -------- Cube --------
st.subheader("Cube")

cube_s = st.number_input("Cube Side", min_value=0.0, key="cube")

col1, col2 = st.columns(2)

with col1:
    st.metric("Surface Area", cube_tsa(cube_s))

with col2:
    st.metric("Volume", cube_vol(cube_s))


st.divider()

# -------- Cuboid --------
st.subheader("Cuboid")

cl = st.number_input("Length", min_value=0.0, key="cub1")
cb = st.number_input("Breadth", min_value=0.0, key="cub2")
ch = st.number_input("Height", min_value=0.0, key="cub3")

col1, col2 = st.columns(2)

with col1:
    st.metric("Surface Area", cuboid_tsa(cl, cb, ch))

with col2:
    st.metric("Volume", cuboid_vol(cl, cb, ch))


st.divider()

# -------- Cylinder --------
st.subheader("Cylinder")

cr = st.number_input("Radius", min_value=0.0, key="cy1")
ch = st.number_input("Height", min_value=0.0, key="cy2")

col1, col2 = st.columns(2)

with col1:
    st.metric("Surface Area", cylinder_tsa(cr, ch))

with col2:
    st.metric("Volume", cylinder_vol(cr, ch))


st.divider()

# -------- Cone --------
st.subheader("Cone")

cone_r = st.number_input("Radius", min_value=0.0, key="co1")
cone_h = st.number_input("Height", min_value=0.0, key="co2")

slant = math.sqrt(cone_r**2 + cone_h**2)

col1, col2 = st.columns(2)

with col1:
    st.metric("Surface Area", cone_tsa(cone_r, slant))

with col2:
    st.metric("Volume", cone_vol(cone_r, cone_h))