import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. METODA LAGRANGE'A
# ==========================================
def lagrange_interpolation(x_data, y_data, x_eval):
    """Oblicza wartości wielomianu Lagrange'a dla punktów x_eval."""
    n = len(x_data)
    y_eval = np.zeros_like(x_eval, dtype=float)
    
    for k in range(len(x_eval)):
        x = x_eval[k]
        y = 0
        for j in range(n):
            p = 1.0
            for i in range(n):
                if i != j:
                    p *= (x - x_data[i]) / (x_data[j] - x_data[i])
            y += y_data[j] * p
        y_eval[k] = y
    return y_eval

# ==========================================
# 2. METODA NEWTONA (Ilorazy różnicowe)
# ==========================================
def newton_interpolation(x_data, y_data, x_eval):
    """Oblicza wartości wielomianu Newtona oraz zwraca tablicę ilorazów."""
    n = len(x_data)
    # Tworzenie tablicy ilorazów różnicowych (Macierz N x N)
    F = np.zeros((n, n))
    F[:, 0] = y_data
    
    # Obliczanie kolejnych rzędów ilorazów różnicowych
    for j in range(1, n):
        for i in range(n - j):
            F[i, j] = (F[i + 1, j - 1] - F[i, j - 1]) / (x_data[i + j] - x_data[i])
            
    # Obliczanie wartości wielomianu dla zadanych punktów
    y_eval = np.zeros_like(x_eval, dtype=float)
    for k in range(len(x_eval)):
        x = x_eval[k]
        y = F[0, 0]
        p = 1.0
        for i in range(1, n):
            p *= (x - x_data[i - 1])
            y += F[0, i] * p
        y_eval[k] = y
        
    return y_eval, F

# ==========================================
# 3. DANE WEJŚCIOWE I WYKRES (z Twoich screenów)
# ==========================================

# Węzły interpolacji (punkty z Arkusza 2/3)
x_points = np.array([-1, 0, 1])
y_points = np.array([2, 1, 3])

# Generowanie gęstej siatki punktów X do narysowania płynnej krzywej
# (od -2 do 2, żeby zobaczyć jak wielomian zachowuje się poza węzłami)
x_plot = np.linspace(-2, 2, 100)

# Obliczenia
y_lagrange = lagrange_interpolation(x_points, y_points, x_plot)
y_newton, ilorazy = newton_interpolation(x_points, y_points, x_plot)

# Wyświetlenie tablicy ilorazów różnicowych (pierwszy wiersz to współczynniki)
print("Tablica ilorazów różnicowych (pierwszy wiersz to współczynniki Newtona):")
print(np.round(ilorazy, 2))

# Rysowanie wykresu
plt.figure(figsize=(8, 5))
# Rysujemy gładką krzywą
plt.plot(x_plot, y_lagrange, label="Wielomian interpolujący (Lagrange/Newton)", color='red', linewidth=2)
# Zaznaczamy nasze węzły
plt.scatter(x_points, y_points, color='blue', zorder=5, label="Węzły interpolacji (dane)")

# Upiększanie wykresu (siatka, osie, legenda)
plt.title("Interpolacja Wielomianowa")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.legend()
plt.show()
