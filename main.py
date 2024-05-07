import requests

def hae_saa(sijainti):
    api_avain = "TÄHÄN_API_AVAIN"  # Täytä tämä omalla API-avaimellasi
    url = f"http://api.openweathermap.org/data/2.5/weather?q={sijainti}&appid={api_avain}&units=metric"
    vastaus = requests.get(url)
    data = vastaus.json()

    if data["cod"] == 200:
        kaupunki = data["name"]
        kuvaus = data["weather"][0]["description"]
        lampotila = data["main"]["temp"]
        kosteus = data["main"]["humidity"]
        tuuli_nopeus = data["wind"]["speed"]

        print(f"Sää kaupungissa {kaupunki}:")
        print(f"Kuvaus: {kuvaus}")
        print(f"Lämpötila: {lampotila} °C")
        print(f"Kosteus: {kosteus}%")
        print(f"Tuulen nopeus: {tuuli_nopeus} m/s")
    else:
        print("Säätilan hakeminen epäonnistui.")

if __name__ == "__main__":
    kaupunki = input("Syötä kaupunki: ")
    hae_saa(kaupunki)

