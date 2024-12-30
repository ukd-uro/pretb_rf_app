def convert_to_text(output):
    psma_string = "Bevorzugt PSMA-PET-CT. Alternativ Ganzkörperknochenszintigraphie und CT-Abdomen und Becken. "
    ct_scintigraphy_string = "Ganzkörperknochenszintigraphie und CT-Abdomen und Becken."
    as_string = "Der Patient erfüllt die Kriterien für eine aktive Überwachung. Falls eine definitive Therapie erwünscht ist, Angebot einer radikalen Prostatektomie oder alternativ perkutane Strahlentherapie."
    rp_rt_string = "Indikation zur radikalen Prostatektomie. Alternativ perkutane Strahlentherapie."
    
    output_string = ""
    
    if output[0] == 1:
        # PSMA
        output_string += psma_string

    if output[1] == 1:
        # CT and bone scintigraphy
        if output[0] == 0:
            output_string += ct_scintigraphy_string
            
    if output[2] == 1:
        # Active Surveillance
        output_string += as_string

    if output[3] == 1:
        # Radical prostatectomy and radiation therapy
        if output[2] == 0:
            output_string += rp_rt_string
    
    return output_string