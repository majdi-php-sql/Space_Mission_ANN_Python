"""
This Neural Network & Code designed & developed by Majdi M. S. Awad

"""

import numpy as np


class NeuralNetwork:
    def __init__(self):
        self.inputs_number = 28
        self.inputs_names = ['space_x', 'boeing', 'martin_marietta', 'us_air_force', 'european_space_agency', 'brazilian_space_agency', 'arianespace', 'falcon', 'delta', 'titan', 'ariane', 'vls', 'vega', 'liftoff_thrust_kn', 'payload_to_orbit_kg', 'rocket_height_m', 'fairing_diameter_m', 'low_earth_orbit', 'geostationary_transfer_orbit', 'medium_earth_orbit', 'sun_synchronous_orbit', 'polar_orbit', 'high_earth_orbit', 'sun_earth_orbit', 'heliocentric_orbit', 'suborbital', 'mars_orbit', 'earth_moon_l2_orbit']

    def calculate_outputs(self, inputs):
        space_x = inputs[0]
        boein_g = inputs[1]
        martin__marietta = inputs[2]
        us_air_fo_rce = inputs[3]
        european_space_agency = inputs[4]
        brazilian_space_agency = inputs[5]
        arianespace = inputs[6]
        falcon = inputs[7]
        delta = inputs[8]
        titan = inputs[9]
        ariane = inputs[10]
        vls = inputs[11]
        vega = inputs[12]
        li_ftoff_thrust_kn = inputs[13]
        payload_to_orbit_kg = inputs[14]
        rocket_height_m = inputs[15]
        fairin_g_diameter_m = inputs[16]
        low_earth_orbit = inputs[17]
        geostationary_transfer_orbit = inputs[18]
        medium_earth_orbit = inputs[19]
        sun_synchronous_orbit = inputs[20]
        polar_orbit = inputs[21]
        high_earth_orbit = inputs[22]
        sun_earth_orbit = inputs[23]
        heliocentric_orbit = inputs[24]
        subo_rbital = inputs[25]
        mars_orbit = inputs[26]
        earth_moon_l_two__orbit = inputs[27]

        scaled_space_x = space_x*(1+1)/(1-(0))-0*(1+1)/(1-0)-1
        scaled_boein_g = boein_g*(1+1)/(1-(0))-0*(1+1)/(1-0)-1
        scaled_martin__marietta = martin__marietta*(1+1)/(1-(0))-0*(1+1)/(1-0)-1
        scaled_us_air_fo_rce = us_air_fo_rce*(1+1)/(1-(0))-0*(1+1)/(1-0)-1
        scaled_european_space_agency = european_space_agency*(1+1)/(1-(0))-0*(1+1)/(1-0)-1
        scaled_brazilian_space_agency = brazilian_space_agency*(1+1)/(1-(0))-0*(1+1)/(1-0)-1
        scaled_arianespace = arianespace*(1+1)/(1-(0))-0*(1+1)/(1-0)-1
        scaled_falcon = falcon*(1+1)/(1-(0))-0*(1+1)/(1-0)-1
        scaled_delta = delta*(1+1)/(1-(0))-0*(1+1)/(1-0)-1
        scaled_titan = titan*(1+1)/(1-(0))-0*(1+1)/(1-0)-1
        scaled_ariane = ariane*(1+1)/(1-(0))-0*(1+1)/(1-0)-1
        scaled_vls = vls*(1+1)/(1-(0))-0*(1+1)/(1-0)-1
        scaled_vega = vega*(1+1)/(1-(0))-0*(1+1)/(1-0)-1
        scaled_li_ftoff_thrust_kn = (li_ftoff_thrust_kn-5318.350098)/2683.75
        scaled_payload_to_orbit_kg = (payload_to_orbit_kg-10130.2002)/8307.179688
        scaled_rocket_height_m = (rocket_height_m-56.05830002)/16.62989998
        scaled_fairin_g_diameter_m = (fairin_g_diameter_m-4.232450008)/1.297140002
        scaled_low_earth_orbit = low_earth_orbit*(1+1)/(1-(0))-0*(1+1)/(1-0)-1
        scaled_geostationary_transfer_orbit = geostationary_transfer_orbit*(1+1)/(1-(0))-0*(1+1)/(1-0)-1
        scaled_medium_earth_orbit = medium_earth_orbit*(1+1)/(1-(0))-0*(1+1)/(1-0)-1
        scaled_sun_synchronous_orbit = sun_synchronous_orbit*(1+1)/(1-(0))-0*(1+1)/(1-0)-1
        scaled_polar_orbit = polar_orbit*(1+1)/(1-(0))-0*(1+1)/(1-0)-1
        scaled_high_earth_orbit = high_earth_orbit*(1+1)/(1-(0))-0*(1+1)/(1-0)-1
        scaled_sun_earth_orbit = sun_earth_orbit*(1+1)/(1-(0))-0*(1+1)/(1-0)-1
        scaled_heliocentric_orbit = heliocentric_orbit*(1+1)/(1-(0))-0*(1+1)/(1-0)-1
        scaled_subo_rbital = subo_rbital*(1+1)/(1-(0))-0*(1+1)/(1-0)-1
        scaled_mars_orbit = mars_orbit*(1+1)/(1-(0))-0*(1+1)/(1-0)-1
        scaled_earth_moon_l_two__orbit = earth_moon_l_two__orbit*(1+1)/(1-(0))-0*(1+1)/(1-0)-1

        perceptron_layer_1_output_0 = np.tanh(-0.0942795 + (scaled_space_x*0.702067) + (scaled_boein_g*-0.0170059) + (scaled_martin__marietta*0.0470749) + (scaled_us_air_fo_rce*-0.427829) + (scaled_european_space_agency*0.186382) + (scaled_brazilian_space_agency*0.00880994) + (scaled_arianespace*-0.278673) + (scaled_falcon*0.636576) + (scaled_delta*-0.0614646) + (scaled_titan*-0.324131) + (scaled_ariane*-0.458031) + (scaled_vls*-0.162932) + (scaled_vega*0.060173) + (scaled_li_ftoff_thrust_kn*0.80247) + (scaled_payload_to_orbit_kg*0.829381) + (scaled_rocket_height_m*1.34109) + (scaled_fairin_g_diameter_m*1.35568) + (scaled_low_earth_orbit*-0.197135) + (scaled_geostationary_transfer_orbit*0.0286355) + (scaled_medium_earth_orbit*0.163854) + (scaled_sun_synchronous_orbit*0.138798) + (scaled_polar_orbit*-0.0997901) + (scaled_high_earth_orbit*-0.198706) + (scaled_sun_earth_orbit*0.0958175) + (scaled_heliocentric_orbit*0.101348) + (scaled_subo_rbital*-0.147103) + (scaled_mars_orbit*0.0317465) + (scaled_earth_moon_l_two__orbit*0.17293))
        perceptron_layer_1_output_1 = np.tanh(-0.491764 + (scaled_space_x*1.35578) + (scaled_boein_g*-0.158264) + (scaled_martin__marietta*0.3356) + (scaled_us_air_fo_rce*0.0413473) + (scaled_european_space_agency*0.18886) + (scaled_brazilian_space_agency*0.194217) + (scaled_arianespace*-0.867198) + (scaled_falcon*1.66176) + (scaled_delta*-0.139305) + (scaled_titan*0.2782) + (scaled_ariane*-0.84669) + (scaled_vls*0.198354) + (scaled_vega*0.404386) + (scaled_li_ftoff_thrust_kn*0.118243) + (scaled_payload_to_orbit_kg*0.272991) + (scaled_rocket_height_m*0.0578778) + (scaled_fairin_g_diameter_m*-0.0430423) + (scaled_low_earth_orbit*0.155079) + (scaled_geostationary_transfer_orbit*0.109792) + (scaled_medium_earth_orbit*0.0583727) + (scaled_sun_synchronous_orbit*0.0664405) + (scaled_polar_orbit*0.079457) + (scaled_high_earth_orbit*0.0191224) + (scaled_sun_earth_orbit*0.0147438) + (scaled_heliocentric_orbit*0.0282534) + (scaled_subo_rbital*-0.0471288) + (scaled_mars_orbit*-0.0697482) + (scaled_earth_moon_l_two__orbit*0.1185))
        perceptron_layer_1_output_2 = np.tanh(-0.531648 + (scaled_space_x*0.453343) + (scaled_boein_g*0.336635) + (scaled_martin__marietta*-0.0716651) + (scaled_us_air_fo_rce*0.324302) + (scaled_european_space_agency*0.296164) + (scaled_brazilian_space_agency*0.0178341) + (scaled_arianespace*0.335198) + (scaled_falcon*0.0456043) + (scaled_delta*0.214565) + (scaled_titan*-0.00297469) + (scaled_ariane*0.159868) + (scaled_vls*0.102542) + (scaled_vega*0.0706866) + (scaled_li_ftoff_thrust_kn*-0.252344) + (scaled_payload_to_orbit_kg*-0.38348) + (scaled_rocket_height_m*-0.247166) + (scaled_fairin_g_diameter_m*-0.266072) + (scaled_low_earth_orbit*0.295134) + (scaled_geostationary_transfer_orbit*0.0491571) + (scaled_medium_earth_orbit*0.251932) + (scaled_sun_synchronous_orbit*0.0438042) + (scaled_polar_orbit*0.0924475) + (scaled_high_earth_orbit*0.113206) + (scaled_sun_earth_orbit*-0.229694) + (scaled_heliocentric_orbit*0.0668757) + (scaled_subo_rbital*0.118162) + (scaled_mars_orbit*-0.0285714) + (scaled_earth_moon_l_two__orbit*-0.0174488))
        perceptron_layer_1_output_3 = np.tanh(-0.348313 + (scaled_space_x*0.62981) + (scaled_boein_g*-0.297083) + (scaled_martin__marietta*0.179946) + (scaled_us_air_fo_rce*0.369039) + (scaled_european_space_agency*0.113605) + (scaled_brazilian_space_agency*0.0992666) + (scaled_arianespace*0.0957783) + (scaled_falcon*-0.118989) + (scaled_delta*0.120721) + (scaled_titan*0.182044) + (scaled_ariane*0.18025) + (scaled_vls*0.124879) + (scaled_vega*-0.0873031) + (scaled_li_ftoff_thrust_kn*-0.0461812) + (scaled_payload_to_orbit_kg*0.148264) + (scaled_rocket_height_m*-0.116362) + (scaled_fairin_g_diameter_m*0.220707) + (scaled_low_earth_orbit*-0.0422787) + (scaled_geostationary_transfer_orbit*0.0750343) + (scaled_medium_earth_orbit*0.0940125) + (scaled_sun_synchronous_orbit*0.0148757) + (scaled_polar_orbit*0.0617457) + (scaled_high_earth_orbit*-0.0830924) + (scaled_sun_earth_orbit*-0.0389896) + (scaled_heliocentric_orbit*-0.0287598) + (scaled_subo_rbital*0.186737) + (scaled_mars_orbit*0.0158954) + (scaled_earth_moon_l_two__orbit*-0.15139))
        perceptron_layer_1_output_4 = np.tanh(-0.258368 + (scaled_space_x*-0.0677492) + (scaled_boein_g*0.586387) + (scaled_martin__marietta*-0.241087) + (scaled_us_air_fo_rce*0.38525) + (scaled_european_space_agency*0.408663) + (scaled_brazilian_space_agency*0.0276632) + (scaled_arianespace*0.12833) + (scaled_falcon*0.0449624) + (scaled_delta*0.0152602) + (scaled_titan*0.206226) + (scaled_ariane*0.216059) + (scaled_vls*-0.190348) + (scaled_vega*0.223277) + (scaled_li_ftoff_thrust_kn*0.36894) + (scaled_payload_to_orbit_kg*-0.215671) + (scaled_rocket_height_m*0.181357) + (scaled_fairin_g_diameter_m*0.165865) + (scaled_low_earth_orbit*0.0700586) + (scaled_geostationary_transfer_orbit*-0.0440892) + (scaled_medium_earth_orbit*0.0895405) + (scaled_sun_synchronous_orbit*0.00730695) + (scaled_polar_orbit*0.091727) + (scaled_high_earth_orbit*0.125706) + (scaled_sun_earth_orbit*-0.0729492) + (scaled_heliocentric_orbit*0.0934075) + (scaled_subo_rbital*-0.122989) + (scaled_mars_orbit*0.00219544) + (scaled_earth_moon_l_two__orbit*0.0619699))

        output = np.array([perceptron_layer_1_output_0, perceptron_layer_1_output_1, perceptron_layer_1_output_2, perceptron_layer_1_output_3, perceptron_layer_1_output_4])
        return output

def main():
    nn = NeuralNetwork()

    print("Please enter the following values:")
    inputs = []
    for name in nn.inputs_names:
        value = float(input(f"{name}: "))
        inputs.append(value)

    outputs = nn.calculate_outputs(inputs)

    print("Predicted Outputs:")
    print(outputs)

if __name__ == "__main__":
    main()