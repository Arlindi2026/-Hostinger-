#!/usr/bin/env python3
"""Builds index.html (English) and es/index.html (Spanish) from src/template.html.
Run: python3 build.py   No dependencies."""
import re, pathlib, sys
root = pathlib.Path(__file__).parent

def items(*xs): return "".join(f"<li>{x}</li>" for x in xs)

EN = dict(
 lang="en", path="/", en_current='aria-current="true"', es_current="",
 meta_title="AV Elite Home Renovation LLC | Home renovation in New York and New Jersey",
 meta_desc="Kitchen and bathroom remodeling, flooring and tile, painting and drywall, and full home renovation in New York and New Jersey. Request a free estimate.",
 skip="Skip to content", nav_label="Sections", lang_label="Language",
 nav_services="Services", nav_work="Work", nav_process="How it works", nav_estimate="Free estimate",
 hero_tape="New York and New Jersey",
 hero_h1="Home renovation, done room by room or all at once.",
 hero_lede="AV Elite Home Renovation LLC remodels kitchens and bathrooms, installs flooring and tile, hangs and finishes drywall, paints, and takes on full home renovations. Tell us what you need. We come see it and give you a free estimate.",
 cta_estimate="Request a free estimate", cta_whatsapp="Message us on WhatsApp",
 slot_hero="Photo of a finished project goes here",
 services_tape="Services", services_h2="What we do",
 s1_name="Kitchens and bathrooms",
 s1_text="A full remodel or a targeted update, from demolition to the last line of caulk.",
 s1_items=items("Cabinets and countertops","Backsplash and wall tile","Vanities, tubs and showers"),
 s2_name="Flooring and tile",
 s2_text="Floors laid flat, lines kept straight, edges and transitions finished clean.",
 s2_items=items("Hardwood, laminate and vinyl plank","Ceramic and porcelain tile","Floors, walls and showers"),
 s3_name="Painting and drywall",
 s3_text="Walls repaired and sanded smooth before any paint goes on.",
 s3_items=items("Interior and exterior painting","Drywall hanging, taping and patching","Skim coating"),
 s4_name="Full home renovation",
 s4_text="One crew for the whole job, planned in order so finished work stays finished.",
 s4_items=items("Several rooms at once","Whole apartments","Whole houses"),
 work_tape="Work", work_h2="Recent projects",
 work_note="Photos from our jobs are being added.",
 slot_kitchen="Kitchen photo", slot_bathroom="Bathroom photo", slot_flooring="Flooring photo", slot_painting="Painting photo",
 process_tape="How it works", process_h2="From first message to final walkthrough",
 p1_name="You tell us about the job", p1_text="Use the form or WhatsApp. Photos of the space help.",
 p2_name="We visit and measure", p2_text="We look at the space in person and talk through what you want.",
 p3_name="You get a free estimate", p3_text="A clear scope and price, so you know what is included.",
 p4_name="We do the work", p4_text="When it is finished, we walk through it with you.",
 est_tape="Free estimate", est_h2="Request a free estimate",
 est_text="Fill in the form and press send. It opens WhatsApp with your details ready, so you only tap send once more.",
 est_wa="Message us on WhatsApp", est_call="Call",
 f_name="Name", f_phone="Phone", f_place="Town or ZIP code", f_service="Service", f_details="About the job",
 f_details_ph="Which rooms, rough size, when you want to start",
 f_submit="Send request on WhatsApp",
 f_note="Nothing is stored on this site. Your request goes straight to our WhatsApp.",
 msg_intro="Hello, I would like a free estimate.",
 foot_area="Serving New York and New Jersey", dock_estimate="Free estimate",
)

ES = dict(EN,
 lang="es", path="/es/", en_current="", es_current='aria-current="true"',
 meta_title="AV Elite Home Renovation LLC | Renovación de casas en Nueva York y Nueva Jersey",
 meta_desc="Remodelación de cocinas y baños, pisos y azulejos, pintura y drywall, y renovación completa de casas en Nueva York y Nueva Jersey. Pida su presupuesto gratis.",
 skip="Ir al contenido", nav_label="Secciones", lang_label="Idioma",
 nav_services="Servicios", nav_work="Trabajos", nav_process="Cómo trabajamos", nav_estimate="Presupuesto gratis",
 hero_tape="Nueva York y Nueva Jersey",
 hero_h1="Renovamos su casa, un cuarto a la vez o toda completa.",
 hero_lede="AV Elite Home Renovation LLC remodela cocinas y baños, instala pisos y azulejos, coloca y termina drywall, pinta y hace renovaciones completas. Cuéntenos qué necesita. Visitamos el lugar y le damos un presupuesto gratis.",
 cta_estimate="Pedir presupuesto gratis", cta_whatsapp="Escríbanos por WhatsApp",
 slot_hero="Aquí va la foto de un proyecto terminado",
 services_tape="Servicios", services_h2="Lo que hacemos",
 s1_name="Cocinas y baños",
 s1_text="Remodelación completa o cambios puntuales, desde la demolición hasta el último sellado.",
 s1_items=items("Gabinetes y encimeras","Salpicaderos y azulejos de pared","Lavamanos, tinas y duchas"),
 s2_name="Pisos y azulejos",
 s2_text="Pisos bien nivelados, líneas rectas, bordes y uniones con buen acabado.",
 s2_items=items("Madera, laminado y vinilo","Cerámica y porcelanato","Pisos, paredes y duchas"),
 s3_name="Pintura y drywall",
 s3_text="Reparamos y lijamos las paredes antes de aplicar la pintura.",
 s3_items=items("Pintura interior y exterior","Instalación, encintado y reparación de drywall","Enlucido fino"),
 s4_name="Renovación completa",
 s4_text="Un solo equipo para todo el trabajo, en el orden correcto, para no dañar lo ya terminado.",
 s4_items=items("Varios cuartos a la vez","Apartamentos completos","Casas completas"),
 work_tape="Trabajos", work_h2="Proyectos recientes",
 work_note="Estamos agregando fotos de nuestros trabajos.",
 slot_kitchen="Foto de cocina", slot_bathroom="Foto de baño", slot_flooring="Foto de pisos", slot_painting="Foto de pintura",
 process_tape="Cómo trabajamos", process_h2="Del primer mensaje a la entrega final",
 p1_name="Usted nos cuenta el trabajo", p1_text="Use el formulario o WhatsApp. Las fotos del espacio ayudan.",
 p2_name="Visitamos y medimos", p2_text="Vemos el espacio en persona y conversamos sobre lo que quiere.",
 p3_name="Recibe un presupuesto gratis", p3_text="Alcance y precio claros, para que sepa qué está incluido.",
 p4_name="Hacemos el trabajo", p4_text="Al terminar, lo revisamos junto con usted.",
 est_tape="Presupuesto gratis", est_h2="Pedir presupuesto gratis",
 est_text="Llene el formulario y presione enviar. Se abre WhatsApp con sus datos listos, solo falta tocar enviar una vez más.",
 est_wa="Escríbanos por WhatsApp", est_call="Llamar",
 f_name="Nombre", f_phone="Teléfono", f_place="Ciudad o código postal", f_service="Servicio", f_details="Sobre el trabajo",
 f_details_ph="Qué cuartos, tamaño aproximado, cuándo quiere empezar",
 f_submit="Enviar pedido por WhatsApp",
 f_note="Este sitio no guarda sus datos. Su pedido llega directo a nuestro WhatsApp.",
 msg_intro="Hola, quisiera un presupuesto gratis.",
 foot_area="Servimos Nueva York y Nueva Jersey", dock_estimate="Presupuesto gratis",
)

NOT_COPY = {"lang", "path", "en_current", "es_current"}
tpl = (root / "src/template.html").read_text()
for d, out in ((EN, "index.html"), (ES, "es/index.html")):
    for k, v in d.items():  # house rule: no dashes in visible copy
        if k not in NOT_COPY and re.search(r"[-–—]", re.sub(r"</?li>", "", v)):
            sys.exit(f"dash in copy: {d['lang']}.{k}: {v}")
    html = re.sub(r"\{\{(\w+)\}\}", lambda m: d[m.group(1)], tpl)
    (root / out).parent.mkdir(exist_ok=True)
    (root / out).write_text(html)
    print("built", out)
