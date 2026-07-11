Biotechnological Strategies for the Recovery of Lithium and Other Metals from a Secondary Source: The Role of Microorganisms and Metal-Binding Peptides

Next Article in Journal

A Carbon Footprint Comparative Analysis of Anaerobic Digestion vs. Landfill Gas Recovery in Brazil

Previous Article in Journal

Study of the Flowability Properties, Morphology and Microstructure of Hazelnut (Corylus avellana L.) Shell Waste Particles Obtained by Milling

Submit to this Journal Review for this Journal Propose a Special Issue

► ▼ Article Menu

## Article Menu

Academic Editors

Zuotao Zhang

Related Info Link

More by Authors Links

Article Views

Citations -

Table of Contents

first_page

Download PDF

settings

Order Article Reprints

Font Type:

Arial Georgia Verdana

Font Size:

Aa Aa Aa

Line Spacing:

  

Column Width:

  

Background:

Open AccessReview

# Biotechnological Strategies for the Recovery of Lithium and Other Metals from a Secondary Source: The Role of Microorganisms and Metal-Binding Peptides

by

Gloria Abigail Martinez-Rodriguez

1 mailto:22040319@itdurango.edu.mx,

Juan Antonio Rojas-Contreras

1,* mailto:jrojas@itdurango.edu.mx,

Perla Guadalupe Vázquez-Ortega

1 mailto:pvazquez@itdurango.edu.mx,

Damián Reyes-Jáquez

1 mailto:damian.reyes@itdurango.edu.mx,

Hiram Medrano-Roldán

1 mailto:hmedrano@itdurango.edu.mx,

Norma Urtiz-Estrada

2 mailto:urtixnue@gmail.com,

Marcelo Barraza-Salas

2 mailto:mbsalas@ujed.mx,

Grisel Fierros-Romero

3 mailto:griselfierrosromero@gmail.com,

Ernesto Rodríguez-Andrade

3 mailto:dc.ernesto.roan@outlook.com and

David Enrique Zazueta-Álvarez

4,* mailto:david.zazueta@unipolidgo.edu.mx

1

Departamento de Ingenierías Química y Bioquímica, TecNM/Instituto Tecnológico de Durango, Blvd. Felipe Pescador 1830 Ote., Durango 34080, Mexico

2

Facultad de Ciencias Químicas, Universidad Juárez del Estado de Durango, Av. Veterinaria s/n. Circuito Universitario, Col. Valle del Sur, Durango 34120, Mexico

3

TecNM/Instituto Tecnológico Superior de Ciudad Hidalgo, Av. Ing. Carlos Rojas Gutierrez 2120, Fracc. Valle De La Herradura, Ciudad Hidalgo 61100, Mexico

4

Departamento de Ingeniería en Tecnología Ambiental, Universidad Politécnica de Durango, Carretera Durango-México Km. 9.5, Durango 34300, Mexico

*

Authors to whom correspondence should be addressed.

Recycling 2026, 11(1), 4; https://doi.org/10.3390/recycling11010004

Submission received: 25 November 2025 / Revised: 18 December 2025 / Accepted: 22 December 2025 / Published: 24 December 2025

(This article belongs to the Topic The Role of Microorganisms in Waste Treatment)

Download keyboard_arrow_down

Browse Figures

<strong>Graphical abstract</strong><br/><strong>Figure 1</strong><br/>
 <p>Mass percentage of the main components of a Li-ion battery.</p><strong>Figure 2</strong><br/>
 <p>Methods for bioleaching metals from lithium-ion battery powder. (<b>a</b>) One step; (<b>b</b>) two step; (<b>c</b>) spent medium.</p><strong>Figure 3</strong><br/>
 <p>Bioleaching mechanisms. (<b>a</b>) Direct mechanisms. Cells adhere to the material through extracellular polymeric substances, and oxidation of sulfides and reduction of metals take place. (<b>b</b>) Indirect mechanisms. Microorganisms do not come into contact with the material, and oxidation and reduction processes occur.</p><strong>Figure 4</strong><br/>
 <p>(<b>a</b>) Bioaccumulation takes place in two steps; in the first step, metals are trapped on the cell surface, and in the second step, they are transported inside the cell by functional groups and trapped by ligands. (<b>b</b>) Biosorption is mediated by the negative charge of the cell wall due to the presence of teichoic acid, phospholipids, and lipopolysaccharides that adsorb metals on the surface.</p><strong>Figure 5</strong><br/>
 <p>Strategies for displaying proteins on (<b>a</b>) the cell surface of <span class="html-italic">Escherichia coli</span>, (<b>b</b>) the spore of <span class="html-italic">Bacillus subtilis</span>, and (<b>c</b>) the cell wall surface of <span class="html-italic">Saccharomyces cerevisiae</span>.</p>

Versions Notes

## Abstract

The growing demand for lithium, driven by its key role in rechargeable batteries and its use in electric vehicles, highlights the need for sustainable and environmentally friendly recovery strategies. Conventional methods, such as pyrometallurgy and hydrometallurgy, are effective but costly and harmful as they emit toxic compounds. Biohydrometallurgy has emerged as a promising alternative, as it uses microorganisms and their metabolites to solubilize metals under milder conditions. Biohydrometallurgy has emerged as a promising alternative, as it relies on microorganisms and their metabolites to solubilize metals under mild operating conditions. Nevertheless, challenges related to process efficiency and selectivity remain, particularly for lithium recovery. In this context, recent advances in metal-binding peptides have attracted increasing attention due to their inherent selectivity and the possibility of rational design and heterologous expression in well-established microbial hosts such as Escherichia coli, Bacillus subtilis, and Saccharomyces cerevisiae. This review critically analyzes current biotechnological strategies and explores the integration of microbial bioleaching with peptide-based approaches as a complementary and environmentally friendly framework for the selective recovery of lithium and other metals from spent batteries and waste electrical and electronic equipment. Overall, this review provides an integrative conceptual framework that highlights the potential of combining microbial processes with metal-binding peptides to guide the development of more selective and sustainable biotechnological strategies for lithium recovery from secondary sources.

Keywords:

bioleaching; metal-binding peptides; lithium; electronic waste; secondary source

Graphical Abstract

## 1. Introduction

Global demand for several metals has increased in recent years, with lithium being one of these elements. Lithium has become an attractive element for the manufacture of rechargeable batteries, as it has a high electrode potential, the highest specific heat capacity of all metals, and serves as an exceptional cathode material [1,2]. In recent years, an annual growth of 11% has been generated in the lithium market, and it is expected to exceed $75 billion by 2025. The extraction of lithium and other critical metals from primary sources may become insufficient at the industrial scale due to increasing demand and source depletion. Consequently, spent lithium-ion batteries have gained attention as an important secondary source, with the potential to partially meet lithium demand while supporting battery circular economy strategies [3,4]. More than 80% of lithium-ion batteries are used in small electronic devices, generating a rapidly growing waste stream. By 2012, this corresponded to approximately 10,700 tons of discarded lithium-ion batteries, a figure that has increased steadily, exceeding an estimated 250,000 tons worldwide by 2020 [5]. In Mexico, the situation is particularly challenging, as current regulations do not establish specific protocols for the recycling of lithium-ion batteries. As a result, spent batteries are often stored by consumers or disposed of in conventional landfills, posing significant environmental risks.

For the recovery of lithium from spent batteries, various physical and chemical methods are used at the industrial level, including pyrometallurgy and hydrometallurgy, but these procedures can be insufficient, costly, and generate significant environmental damage [6]. From this, biohydrometallurgy arises as an effective, low-cost, and environmentally friendly method, since it uses microorganisms and their metabolites for the recovery of metals, eliminating the dependence on harmful chemical compounds [3,7].

The microorganisms used in biohydrometallurgical processes generally come from extreme environments and are capable of solubilizing the metals in mining tailings or electronic waste by oxidizing iron or reducing sulfur, which they use as an energy source [8]. They produce biogenic acids, extracellular polymeric substances (EPS), and proteins, among other compounds, which facilitate the solubilization of metals by various mechanisms, such as acidolysis, redoxolysis, complexation, bioaccumulation, or biosorption [9]. Despite the advantages of the use of microorganisms, they still present certain disadvantages as a limited process due to slow kinetics and the difficulty of scaling up the processes.

New strategies for the recovery of metals have been sought, thus emerging the design and application of metal-binding peptides, which can recover metals from the leached medium in a fast, simple, and specific way. They can also be produced recombinantly to facilitate their production, characterization, and purification [10]. In addition, the immobilization of the binding peptide on a solid support would improve its stability and handling, as well as allow its recovery, reuse, and application in industrial processes [11]. In this context, Selvamani et al. [4] constructed a lithium-binding peptide displayed on the surface of Escherichia coli, showing a high selectivity for lithium over other metals such as cobalt, chromium, and copper; likewise, Jeong et al. [12] applied the same binding peptide for the recovery of lithium ion spent batteries, observing a high selectivity for lithium.

Recent reviews on metal recovery have focused mainly on pyrometallurgy, hydrometallurgy, and biohydrometallurgy processes. Therefore, this review offers a novel and integrative perspective by jointly analyzing the role of microorganisms and metal-binding peptides as complementary biotechnological tools for the recovery of lithium and other metals from secondary sources. Beyond a descriptive compilation, this work compares the mechanisms, advantages, and limitations of microbial processes and peptide-based strategies, highlighting how their combined or sequential application could improve metal selectivity, recovery efficiency, and process sustainability. Furthermore, this review places a specific emphasis on secondary sources, aligning biotechnological advances with the principles of the circular economy. By identifying key knowledge gaps and discussing future research directions, particularly with regard to peptide design.

The literature analyzed in this review was selected through an exhaustive bibliographic search conducted in the main scientific databases, including Science Direct, MDPI, Wiley, Springer, and PubMed. The search strategy combined keywords related to lithium recovery, secondary sources, biotechnological processes, microorganisms, and metal-complexing peptides. Priority was given to peer-reviewed articles published in the last 10–15 years, with a special emphasis on studies addressing lithium recovery from spent lithium-ion batteries and other secondary sources. Finally, the selected studies were evaluated based on their relevance to biotechnological mechanisms, recovery efficiency, and application in secondary sources.

Therefore, the objective of this review is to critically analyze and integrate current biotechnological strategies for the recovery of lithium and other metals from secondary sources, with special emphasis on the role of microorganisms and metal-binding peptides, to identify the main challenges, knowledge gaps, and future lines of research for achieving sustainable and selective metal recovery.

## 2. Secondary Sources of Lithium and Other Metals

Lithium can be obtained from primary sources such as minerals, clays, brines, and seawater [2,6]. In nature, lithium is not found in its free form but can be found in conjunction with igneous rocks and springs [6]. It is present in a wide range of minerals (approximately 145 mineralogical species); however, only a few have economic value, the main ones being spodumene, amblygonite, lepidolite, and petalite [13]. Nevertheless, they represent a primary non-renewable source of supply, which will gradually be depleted due to constant exploitation [9].

Lithium and other important metals can also be found in secondary sources such as batteries and electronic waste, which have the potential to be a low-cost and environmentally friendly alternative to primary sources and can reduce the consumption of natural sources [14]. However, secondary sources do not have effective and selective recycling methods for recovering the metals of interest.

### 2.1. Spent Lithium-Ion Batteries (LIBs)

Spent lithium-ion batteries (LIBs) are considered hazardous waste due to the presence of toxic compounds in their cathode material, which consists of an aluminum plate coated with a mixture of various compounds such as lithium cobalt oxide (LiCoO2), manganese (LiMn2O4) or nickel (LiNiO2)4; as well as an anode generally consisting of graphite or lithium titanate (LTO, Li4Ti5O12) [6,15,16,17]. In addition, it has an electrolyte solution made up of lithium salts such as lithium hexafluorophosphate (LiPF6), lithium perchlorate (LiClO4), lithium tetrafluoroborate (LiBF4), or lithium hexafluoro arsenate (LiAsF6). However, upon reaction to water, they can easily release noxious gases such as hydrofluoric acid (HF) and phosphorus pentafluoride (PF5) [16,18,19]. Finally, plastic materials make up the cover, as well as aluminum and copper sheets [8].

The total percentage of battery components is 35% cathode, 25–30% battery shell, 15–18% anode, 11–12% electrolytes, 5–6% plastic materials, and 3–4% others, as shown in Figure 1 [8]. Lithium cobalt oxide (LiCoO2) is generally the cathode material of choice due to its high specific energy density and durability, and can contain more than 20% Co and 7% Li of the total mass [15].

The global demand for LIB is increasing rapidly every year, with an annual growth rate of 30%, and by 2030, demand is expected to increase 14-fold, driven by the electrification of vehicles [16]. However, this growth raises concerns about the environment and the end-of-life management of these potentially hazardous wastes, thus requiring efficient recycling methods with low environmental impact [20].

### 2.2. Waste Electrical and Electronic Equipment (WEEE)

In 2016, an estimated 44.7 million metric tons of electronic waste were generated worldwide, with an annual growth rate of approximately 3–4% [21]. By 2017, however, only 46% of this waste was recycled, indicating that the majority was released into the environment.

WEEE contains a wide range of hazardous metals and compounds, including mercury, cadmium, lead, arsenic, hexavalent chromium, polybrominated biphenyls, and polychlorinated biphenyls, all of which pose risks of contaminating water, air, and soil. Additionally, incineration of WEEE can generate and release toxic substances such as dioxins, furans, polycyclic aromatic hydrocarbons, polyhalogenated aromatic hydrocarbons, and hydrogen chloride.

On average, WEEE is composed of 40–70% metals, consisting primarily of base metals such as iron (Fe), copper (Cu), nickel (Ni), aluminum (Al), and lead (Pb) [22]. It also contains smaller quantities of precious metals, including silver (Ag), gold (Au), platinum (Pt), and palladium (Pd). Among these, silver and gold are the most abundant in most electrical and electronic equipment [23].

WEEE are generally recycled using pyrometallurgical and hydrometallurgical methods due to the presence of heavy metals, and are considered a valuable secondary source; however, these methods are undesirable due to the difficulty of controlling the secondary waste produced, the high cost, and the risks associated with the process [14]. Employing environmentally sustainable recovery processes would not only reduce pollution but also contribute to economic and environmental sustainability [21].

## 3. Microorganisms in Lithium and Other Metals Recovery

Bioleaching is a process that uses microorganisms for the recovery of valuable metals from LIBs and WEEE, which produce organic and inorganic acids for the treatment of waste, causing the metals to be leached due to a change in their solubility [7,18,21]. This particular method consumes little energy, is environmentally friendly, has a good cost–benefit ratio, generates low emissions of toxic gases, and the process of handling microorganisms is simple and becomes selective [14,19]. A disadvantage of this process is that it requires long reaction times, slow kinetics, and difficulty in culturing the microorganisms [6,7]. However, bioleaching has been applied effectively in the mining industry by oxidation of sulfide minerals with autotrophic organisms [24].

### 3.1. Bioleaching Microorganisms

Various microorganisms are used in lithium bioleaching, which can convert insoluble solids to soluble extractable forms. These can be classified into different groups according to their energy source, such as chemolithotrophs, chemoorganotrophs, etc. [9,14].

Chemolithotrophic microorganisms are generally acidophilic as they thrive in media with pH values below 2, employ inorganic compounds as their energy source, and utilize carbon dioxide (CO2) as their carbon source [8]. Their energy comes from the oxidation of ferrous ion (Fe2+) as well as the reduction of sulfurous compounds such as sulfuric acid (H2SO4) and elemental sulfur (S0) [3,6]. Through the generation of an acidic medium, they promote the solubilization of metals, which occurs through the ferric ion (Fe3+), which accelerates the production of sulfuric acid and thus the solubilization of metals to the surface [21].

Among the species belonging to this classification are the genera Leptospirillum sp. and Acidithiobacillus sp., the most commonly used being A. ferrooxidans, A. thiooxidans, and L. ferrooxidans [6]. Several studies have been conducted employing A. thiooxidans, where 99% Li recovery was achieved from used coin or button batteries with a pulp density of 30 g/L [25], and A. ferrooxidans for the recovery of cobalt and manganese from spent button batteries in different S/L ratios. With an S/L ratio of 40 g/L, recovery rates of 100%, 88%, and 20% were obtained for lithium, cobalt, and manganese, respectively [26]. Additionally, A. ferrooxidans was utilized for the bioleaching of NCM lithium-ion batteries. The analysis showed recoveries of 90% Ni, 92% Mn, 82% Co, and 89% Li in 72 h with a pulp density of 100 g/L. The A. ferrooxidans culture was efficient during three repositioning cycles [27]. Also, 93.64% Li recovery from LIBs was obtained by a sulfide-oxidizing bacterium isolated from a mining well [28]. Finally, studies have been conducted to analyze the effects of bacterial energy sources, such as Fe2+, pyrite, and S0, and bacterial oxidation products, such as Fe3+ and sulfuric acid, on the chemical leaching of LiCoO2. The results indicated that lithium was dissolved with acid, and cobalt was released by Fe2+ reduction and acid dissolution. The recovery of Li+ and Co2+ could be significantly improved by adjusting the pH. The optimal recovery of Li+ and Co2+ in the pyrite group reached 91.4% and 94.2%, respectively. With pyrite as an energy source, the bacteria produced sulfuric acid, and the recovery of lithium and cobalt could be increased to 100% and 99.3% by bacteria. In addition, it was observed that extracellular polymeric substances improved the recovery of Li+ and Co2+ [29].

On the other hand, chemoorganotrophic or heterotrophic microorganisms use organic compounds as their energy source and carbon-based materials as their carbon source [8]. Within this group, there are filamentous fungi such as Aspergillus sp. and Penicillium sp., and cyanogenic bacteria [21]. Fungal bioleaching is carried out by two main mechanisms: the secretion of metabolites such as malic, lactic, oxalic, citric, succinic, pyruvic, tartaric, and formic acid, and the accumulation of metal ions in vacuoles. They can perform their functions over a wide pH range of 3–7 and have a high tolerance to metal toxicity, a shorter adaptation phase, and a rapid leaching rate [8]. Commonly, fungi perform metal solubilization by acidolysis, complexolysis, and redoxolysis [9,19].

The microorganisms belonging to the cyanogenic group are the genera Pseudomonas sp., Bacillus sp., and Escherichia sp., as well as fungi of the genera Clitocybe sp. and Polysporus sp., which can carry out the bioleaching process at pH values of 7–11 and temperatures between 25 and 35 °C [21]. The mechanism they employ consists of using glycine as a precursor and producing hydrogen cyanide, which forms complexes with the metals and confers solubility and stability [6].

Research with fungi has yielded favorable results in the recovery of lithium from LIBs. Aspergillus niger was compared with Acidithiobacillus thiooxidans in the bioleaching process, resulting in 100% Li recovery with the fungal strain, while 66% with the bacterial strain [15]. On the other hand, when using three fungal strains, Aspergillus niger, Penicillium chrysogenum, and Penicillium simplicissimum in the bioleaching of LIBs, it was observed that high concentrations of organic acids were excreted, which increased the bioleaching efficiency [30]. Aspergillus niger was evaluated for the detoxification and recovery of Cu, Li, Mn, Al, Co, and Ni metals from spent lithium-ion batteries from mobile phones under various conditions (one-step, two-step, and spent medium). A recovery efficiency of 100% was obtained for Cu, 95% for Li, 70% for Mn, 65% for Al, 45% for Co, and 38% for Ni at a pulp density of 1% in the spent medium bioleaching [19].

Also, native bacteria have shown potential in recovering metals from LIBs. Bacterial strains isolated from the soil of Mount Merapi achieved a lithium recovery of 62.83% after 15 days, with a soil/battery mass ratio of 100 g/100 g, pulp density of 2 mg/mL, initial pH of 7, temperature of 30 °C, and stirring speed of 120 rpm. In addition, the adaptation of the bacteria to LiCl was observed [31]. Another study used Gluconobacter oxydans isolated from corn stover and iron (II) as a reducing agent for the bioleaching of LIBs cathodes (black mass), where the techno-economic analysis (TEA) estimated an average potential profit margin of approximately 21% for the processing of 10,000 t of black mass per year, corresponding to nearly 30% of the black mass available in the United States in 2020. In parallel, the life cycle assessment (LCA) indicated that the bioleaching of LIBs may offer improved environmental sustainability compared to alternative hydrometallurgical recovery routes, such as hydrochloric acid leaching, exhibiting a substantially lower global warming potential (16–19 kg versus 43–91 kg CO2-equivalent per kilogram of cobalt recovered) [32]. Finally, a culture of Acidithiobacillus and Alicyclobacillus spp. native to sediments from a highly acidic mining lake gradually adapted to increasing concentrations of Li+, Co2+, Ni2+, Mn2+, and Cu2+, where recovery rates of up to 100% of Li, Co, Ni, Mn, and Al form spent NMC-LIB were achieved through two-step bioleaching using the adapted culture, resulting in more efficient metal extraction in comparison with bioleaching with a non-adapted culture and an abiotic control [33].

### 3.2. Bioleaching Methods

Bioleaching can be carried out using three main approaches: one-step, two-step, and spent-medium. In the conventional one-step process (Figure 2a), the inoculum of a previously grown culture is brought directly into contact with the material to be leached. This approach is operationally simple but may be limited by metal toxicity and reduced microbial activity at high pulp densities [8,15]. In the two-step method (Figure 2b), microorganisms are first grown to the logarithmic phase to promote the production of bioacids, after which the material is added; this strategy allows better control of microbial growth and metabolite production but increases process time and operational complexity [14,15]. In the spent-medium approach (Figure 2c), microorganisms are cultivated to the stationary phase to maximize metabolite production, followed by cell removal via centrifugation or filtration, and subsequent contact of the cell-free medium with the material to be leached. This method minimizes metal toxicity effects on microorganisms and enables the use of higher pulp densities; however, it requires additional separation steps [8].

Several studies have reported higher metal recovery efficiency through the spent-medium approach [15,34]. The quality and quantity of biogenic acids can be increased during the initial growth phase without microbial inhibition by metals [8].

### 3.3. Bioleaching Mechanisms

Lithium bioleaching can be classified into two categories: direct and indirect, referring to the physical contact or non-contact of microorganisms with solid materials, whose mechanism is mediated by three fundamental processes: acidolysis, redoxolysis, and complexolysis [6,21]. In direct contact (Figure 3a), the microorganisms are absorbed into the suspension of the material in just a few minutes or hours, and the process is carried out by sulfide oxidation or reduction of metals (redoxolysis), as well as electron transfer from the metal to the cell [6,8,21], as shown in Equations (1) and (2).

F e S 2 + 3.5 O 2 + H 2 O → F e 2 + + 2 H + + 2 S O 4 2 −

(1)

2 F e 2 + + 0.5 O 2 + 2 H + → 2 F e 3 + + H 2 O

(2)

During the process of bioleaching and oxidation-reduction reactions, extracellular polymeric substances (EPS) are formed, which consist of polysaccharides, glycoproteins, lipopolysaccharides, phospholipids, and uronic acid humic substances that lead to the generation of biofilms [9]. These EPS mediate the adhesion of the cells on the surface of the material employing hydrophobic and electrostatic forces, which are generated by the positive charge created by the Fe3+ chelate [6].

Another mechanism is indirect bioleaching (Figure 3b), where microorganisms carry out the process by oxidizing and reducing agents, such as organic and inorganic acids [6,8]. In this process, microorganisms do not need to come into contact with the metals since they are only involved in the production of leaching agents, such as sulfuric, citric, gluconic, oxalic, and malic acids [6]. This process involves the oxygen that coats the surface of the insoluble metal, which is protonated and solubilized through an acid compound. Once the oxygen is protonated, it can interact with the water, favoring the release of the metals into solution [21]. Also, ferric ion is employed as an oxidant that is reduced to ferrous ion, as well as complexation or complexolysis with organic acids to form stable compounds [6,8]. The mechanisms of indirect bioleaching are defined in Equations (3)–(5), where M represents a bivalent metal.

F e S 2 + 14 F e 3 + + 8 H 2 O → 15 F e 2 + + 16 H + + 2 S O 4 2 −

(3)

M S + 2 F e 3 + → M 2 + + S 0 + 2 F e 2 +

(4)

S 0 + 1.5 O 2 + H 2 O → 2 H + + S O 4 2 −

(5)

Lithium bioleaching from LIBs appears to be carried out via a sulfide oxidation mechanism with the production of sulfuric acid, which is independent of EPS formation and rather mediated by the acidolysis process [35], while the removal of metals such as Co, Mn, and Ni is carried out via the direct contact mechanism [8].

In the case of lithium extraction from lithium oxide and cobalt batteries, the process can be carried out by oxidation of iron or sulfides, as shown in Equations (6) and (7) [6].

4 L i C o O 2 + 12 H + → 4 L i + + 4 C o 2 + 6 H 2 O + O 2

(6)

2 F e S O 4 + 2 L i C o O 2 + 4 H 2 S O 4 → F e 2 ( S O 4 ) 3 + 2 C o S O 4 2 + L i 2 S O 4 + 4 H 2 O

(7)

Table 1 summarizes the main studies on the bioleaching of different types of LIBs, with particular emphasis on the microbial groups employed, including acidophilic and chemoorganotrophic microorganisms, the bioleaching approaches applied, and the most relevant results obtained.

## 4. Biotechnological Approaches for Metal Recovery

The reactions resulting from the bioleaching process facilitate the extraction of metals from the solid matrices in which they are found, thus transforming the hazardous parts into non-hazardous forms. At the industrial level, the processes mainly used for metal recovery are chemical precipitation and electrodeposition. However, chemical precipitation has low selectivity, generates large volumes of sludge, and requires waste treatment, while electrodeposition has high energy consumption, is inefficient for highly diluted solutions, and requires specialized equipment [36]. For this reason, biotechnological strategies such as biosorption and bioaccumulation have been developed to mitigate environmental impact and improve selectivity for metals [9].

### 4.1. Bioaccumulation

Bioaccumulation is a process that occurs in living microorganisms [37,38]. It is an active process in which various microorganisms, such as bacteria, algae, and fungi, are capable of bioaccumulating metals [37,39]. It is mediated by the metabolism of living microorganisms in conjunction with intracellular absorption and bioprecipitation mechanisms [9]. Microorganisms can absorb metals through direct contact with the environment or indirectly by ingesting nutrients through the same entry pathways [37].

This process occurs in two stages; in the first stage, the metals are trapped on the cell surface, and then in the second stage, they are transported inside through the lipid membrane, facilitated by various functional groups such as amino, carboxyl, hydroxyl, phosphate, and sulfate groups [8,37]. Once inside the intracellular space, the metals are trapped by ligand proteins and peptides, as shown in Figure 4a [39].

Bioaccumulation by microorganisms has been reported in lithium bioleaching processes, as in the study by Sedlakova-Kadukova et al. [40], where lepidolite was bioleached using three microbial systems, observing lithium bioaccumulation in processes mediated by the fungi Aspergillus niger and Rhodotorula mucilaginosa. The largest amount of lithium was accumulated by R. mucilaginosa cells, representing 92% of the total amount of Li recovered from minerals. In the case of the fungus A. niger, the biomass produced accumulated 77% of the total solubilized Li. On the other hand, Tsuruta [41] investigated the bioaccumulation of lithium by various microorganisms, observing that strains of the bacteria Arthrobacter nicotianae and Brevibacterium helovolum showed a high capacity for lithium accumulation, with lithium accumulation by A. nicotianae cells being greatly affected by the pH of the solution, with maximum lithium accumulation occurring at pH 6.

Other studies investigated the absorption of heavy metal ions by Pseudomonas aeruginosa isolated from the Persian Gulf, with the highest adsorption for Cu, Zn, Cd, and Pb, respectively. The strain accumulated heavy metals in the cell wall and along the outer cell surfaces through surface phenomena such as diffusion [42]. The study carried out by Arifiyanto et al. [43] examined the bioaccumulation levels of Pb2+ by Bacillus isolates. The microbial isolate achieved a bioaccumulation efficiency rate of up to 53% in the presence of lead concentrations (75 and 100 mg/L). Likewise, a protein of ±127 kDa was detected in the presence of lead and low molecular weight proteins, around 14 kDa, related to metallothioneins and heat shock proteins associated with metal resistance. Aslam et al. [44] identified three bacterial strains as Stenotrophomonas sp., Klebsiella pneumoniae, and Staphylococcus sp., capable of tolerating 700–1000 μg/mL of Ni, 500–1000 μg/mL of Cr, and 1000–1600 μg/mL of Pb, respectively, with a gradual increase in the percentage of accumulation overtime due to the increase in biomass. Therefore, these studies demonstrate the ability of indigenous bacteria to treat environments contaminated with metals.

Accordingly, bioaccumulation has certain advantages, such as intracellular sequestration capacity, the potential to selectively retain metals, and its usefulness as an indicator of metal exposure. However, it also has limitations related to cellular structure or architecture, such as gene and protein expression levels, and stress response due to toxic components in the environment [37,39].

### 4.2. Biosorption

Biosorption involves the use of biological matrices, including living or dead microorganisms, metal-binding peptides, plant-derived materials, biopolymers, agro-industrial wastes, sludge, or combinations thereof [38]. This process occurs through mechanisms such as adsorption, ion exchange, complexation, chelation, reduction, and precipitation, enabling the recovery of metal ions from leachates under a wide range of environmental conditions [12].

Biosorption is strongly influenced by the physicochemical properties of microbial cell walls. Gram-positive bacteria possess thick peptidoglycan layers enriched with negatively charged functional groups, whereas Gram-negative bacteria contain lipopolysaccharides, phospholipids, and teichoic acids that also contribute to cation binding (Figure 4b) [9]. Among its main advantages, biosorption relies on inexpensive biomass, allows multi-metal capture, operates across broad pH and temperature ranges, and facilitates metal desorption without the need for additional chemical reagents [45].

#### Cell Surface Display as an Enhanced Biosorption Strategy

Cell surface display has emerged as an advanced biosorption strategy in which specific binding proteins or peptides are genetically anchored to the microbial surface using native membrane or cell wall proteins. This approach enables the direct exposure of functional binding motifs to the external environment, enhancing selectivity and adsorption efficiency while avoiding extensive downstream purification steps [10].

Model microorganisms such as Escherichia coli, Bacillus subtilis, and Saccharomyces cerevisiae have been widely used as hosts for surface display systems. In E. coli, outer membrane proteins (OMP) and autotransporters have been employed to anchor metal-binding peptides (Figure 5a), including lithium-binding sequences that exhibited high selectivity over competing metals in synthetic multi-metal solutions and battery-related systems [4,12]. However, limitations related to protein folding and disulfide bond formation have been reported [46].

Gram-positive hosts such as Bacillus subtilis are non-pathogenic bacteria commonly found in soil, classified as a generally recognized safe (GRAS) organism, and capable of forming spores [47]. The use of spores avoids the problems of protein misfolding caused by crossing through membranes since the proteins present in the outer layer of the spore do not cross membranes [46]. Spores withstand extreme physical and chemical changes such as heating, desiccation, radiation, ultraviolet light, oxidizing agents, and lytic agents such as enzymes and can remain viable for many years [48].

Through surface expression strategy, B. subtilis spores can be applied for various biotechnological strategies such as the production of vaccines, biosorbents, catalytic biosensors, and application in bioremediation through the fusion of specific peptides with spore coat proteins (CotA, B, C, etc.), as shown in Figure 5b [46,47,48,49,50].

Similarly, Saccharomyces cerevisiae, which is classified as a GRAS microorganism, has been employed for cell surface protein expression, as it has a large relative cell size, rigid walls, and is capable of post-translational modifications for heterologous protein expression [51]. Yeast surface display systems based on glycosylphosphatidylinositol (GPI) anchors and flocculation proteins (Flo1) have enabled the immobilization of metal-binding proteins, enhancing the adsorption of metals (Figure 5c) [52,53]. Wei et al. [54] observed that four types of metallothioneins from Solanum nigrum were expressed on the cell surface of S. cerevisiae using an α-agglutinin-based anchoring system to adsorb ultra-trace cadmium effectively. Similarly, Wei et al. [51] expressed MerR on the cell surface, making the adsorption capacity of S. cerevisiae to Hg2+ much higher than that of the original and control strains.

Collectively, cell surface display strategies provide a versatile platform for the presentation of metal-binding peptides, serving as a conceptual and technological bridge between conventional biosorption and the development of highly selective peptide-based recovery systems, which are discussed in the following section.

In addition to bioaccumulation and biosorption, bioprecipitation represents another biotechnological mechanism for metal recovery. Unlike bioaccumulation, which involves the intracellular uptake of metals, and biosorption, which relies on surface interactions between metal ions and functional groups, bioprecipitation is mediated by microbial redox activity or metabolic byproducts that induce the formation of insoluble metal phases [55].

Bioprecipitation is most commonly associated with sulfate-reducing bacteria (SRB), which generate biogenic sulfides as a result of anaerobic sulfate reduction. In this process, sulfates serve as terminal electron acceptors, while simple organic compounds act as electron donors, leading to the production of sulfide species capable of precipitating dissolved metals as metal sulfides [55,56]. Several studies have demonstrated the effectiveness of SRB-driven bioprecipitation for the removal of metals from leachates derived from secondary sources. For example, Calvert et al. [57] reported the biological precipitation of dissolved metals from LIB leachates using a dynamic bioreactor consortium dominated by Desulfovibrio. The system achieved average dissolved sulfide concentrations of 507 mg L−1 and sulfate reduction rates of 278 mg L−1 d−1, resulting in precipitation efficiencies exceeding 99% for Al, Ni, Co, and Cu, which together accounted for 96% of the total metal value in the leachate.

Similarly, Yken et al. [58] evaluated metal recovery from printed circuit board waste leachates using hydrogen sulfide generated by an SRB consortium in a fluidized bed reactor. The biogenic sulfide, in combination with NaOH, enabled precipitation efficiencies above 99% for Al, Ni, Cu, and Zn. In another study, Dong et al. [59] investigated the removal of Pb(II) and Zn(II) from aqueous solutions and tailings sand using SRB. While SRB showed strong removal capacity for Zn(II) at concentrations up to 40 mg L−1, higher concentrations inhibited microbial growth. In contrast, Pb(II) removal efficiencies reached 100% at concentrations between 10 and 50 mg L−1, highlighting the metal-specific performance of SRB-mediated bioprecipitation.

Although bioprecipitation is not directly applicable to lithium recovery due to the redox-inactive nature of Li+, this mechanism can indirectly enhance lithium recovery by selectively removing competing metals from complex leachates. By reducing metal interference, bioprecipitation can improve the efficiency and selectivity of subsequent bioaccumulation or biosorption processes, including peptide-based strategies. Consequently, bioprecipitation should be considered a complementary approach within integrated biotechnological frameworks, particularly for complex secondary sources such as LIBs and WEEE.

## 5. Metal-Binding Peptides for Metal Recovery

Metal-binding peptides have emerged as an innovative area of research, which has gained great interest in metal recovery, soil remediation, water remediation, and biosorption processes. The use of metal-binding peptides has the advantage of reducing environmentally harmful chemicals and the generation of toxic products [38,60].

Peptides are more resistant to extreme environmental conditions and have greater specificity for metals, avoiding interference with other competing ions. Also, they can be immobilized on reusable supports, compared to microbial systems that often require cell destruction for metal recovery. In biomining, peptides have been used for the recovery of metals such as gold, copper, or nickel [38]. Metallothioneins (MTs), phytochelatins, and metal regulatory proteins from diverse organisms, including bacteria, fungi, plants, animals, and humans, have been expressed in microbial hosts to enhance the removal of various metal ions from contaminated media [60].

Metallothioneins (MTs) are a group of low molecular weight (6–10 kDa) proteins rich in cysteine residues (Cys-Cys, Cys-X-Cys, or Cys-X-X-Cys; X is an amino acid different from cysteine) with a structure lacking aromatic amino acids and histidines. Its main function is to detoxify the cells of heavy metals, protect against oxidative stress, and maintain homeostasis [60]. Ruta et al. [61] successfully expressed MTs from Arabidopsis thaliana and Noccaea caerulescens in the inner part of the plasma membrane of Saccharomyces cerevisiae, showing increased accumulation of various metals such as Cu, Zn, Mn, Ni, Co, and Cd. Deng et al. [62] expressed MTs from peas and the NiCoT transporter protein of Helicobacter pylori in E. coli with increased Ni bioaccumulation in the presence of Na, Co, and Cd.

On the other hand, phytochelatins are cysteine-rich peptides that are responsible for metal capture and detoxification to maintain intracellular homeostasis in various plants and microorganisms. Their structure consists of Glutamate (Glu) and Cysteine repeats with a Glycine (Gly) residue [60]. Li et al. [63] overexpressed the PcPCS1 gene from Pyrus calleryana, encoding phytochelatin synthase, in E. coli with increased accumulation of Cd, Cu, and Hg.

Metal regulatory proteins, also referred to as metal detector proteins, specialize as regulatory proteins that control the expression of metal chaperone-associated genes, metal importers, and metal expulsion transporters that regulate metal bioavailability [60]. In this context, Hui et al. [64] engineered an E. coli strain capable of expressing the lead (Pb) binding domain on its cell surface, which was able to selectively adsorb Pb in the presence of Cd and Zn. Finally, Tang et al. [65] developed Pseudomonas aeruginosa cells capable of expressing cadmium-induced regulatory protein CadR on their surface, with enhanced Cd adsorption, as shown in Table 2.

To date, only a limited number of studies have explored peptide-based strategies for lithium recovery from secondary sources related to lithium-ion batteries. Most of these works focus on proof-of-concept systems using synthetic multi-metal solutions or battery-derived wastewaters rather than direct treatment of solid cathode materials.

Selvamani et al. [4] engineered E. coli to display a lithium-binding peptide (LBP, GPGAP) on the cell surface using OmpC as an anchoring motif. By constructing dimeric, trimeric, and tetrameric peptide repeats, the authors significantly enhanced lithium adsorption, with the trimeric construct achieving the highest uptake (3240.2 µmol g−1 DCW at 20 mM LiCl) and high selectivity over competing metals such as Co, Cr, and Cu. Importantly, this system was validated using both artificial wastewater and lithium-containing battery wastewater obtained by aqueous leaching, demonstrating selective lithium recovery and reduced phytotoxicity of the treated effluent. In addition, Selvamani et al. [66] also reported the adsorption of lithium as surface-associated nanoparticles through the display of a lithium-binding peptide on recombinant E. coli, further supporting the feasibility of peptide-mediated lithium capture at the cell interface.

Similarly, Jeong et al. [12] reported the surface display of a lithium-binding peptide (LBP1) on E. coli via OmpC, systematically evaluating environmental parameters and peptide multimerization. The trimeric construct showed superior lithium recovery and selectivity in synthetic NCM (Ni–Co–Mn) solutions and real industrial lithium battery wastewater, highlighting the robustness of peptide-based biosorption under competitive metal conditions.

Beyond whole-cell systems, Bhargawa et al. [67] developed reusable magnetic beads functionalized with lithium-binding peptides, achieving adsorption capacities up to 85.5 mg Li g−1 of bead and a maximum Langmuir capacity of 126.3 mg Li g−1. These peptide-based materials maintained over 72% of their initial adsorption capacity after six adsorption–desorption cycles and exhibited high lithium selectivity in the presence of competing metal ions, demonstrating their potential for scalable aqueous recovery systems.

Collectively, these studies demonstrate that metal-binding peptides enable highly selective lithium recovery from complex aqueous matrices. However, their application has largely been limited to synthetic solutions or simplified battery-derived wastewaters, underscoring the need to integrate peptide-based biosorption with upstream biotechnological processes such as bioleaching to address real LIB residues.

## 6. Challenges and Future Perspectives for Research

The role of microorganisms and the use of metal-binding peptides for the recovery of lithium and other metals from secondary sources, such as LIBs and WEEE, represent an emerging area with great potential. However, it still faces challenges for large-scale consolidation. Nevertheless, it is possible to identify several lines of research that could guide future development in this area.

Process scaling: the industrial-scale bioleaching of LIBs and WEEE remains challenging due to slow process kinetics, long residence times, and limited metal selectivity during recovery. These constraints negatively impact process productivity and economic feasibility. Addressing these limitations requires the optimization of operational parameters and strategies aimed at reducing microbial adaptation and activation times. In this context, advances in bioreactor design, together with the development and adaptation of strains to high metal concentrations, are expected to enhance process stability and improve metal recovery efficiency at larger scales.

Optimization of microorganisms used in the bioleaching process: for this purpose, the application of genetic engineering tools would allow the design of strains with greater tolerance to high metal concentrations and with selective solubilization capacity for certain metals. In addition, the improvement and adaptability of microbial consortia could lead to superior and reproducible bioleaching efficiency.

Design of metal-binding peptides: using bioinformatics tools and complementing them with learning and simulation models opens up the possibility of predicting and synthesizing peptides with high specificity for lithium or other metals, minimizing the adsorption of competing cations. Also, the area of metal-binding peptides requires further research, using immobilization techniques that confer stability and reusability of the molecules under industrial conditions, including solid supports such as membranes, polymers, or nanomaterials, since improving stability under conditions of pH, temperature, and components resulting from leaching is crucial to ensuring the success of the process.

Collectively, these perspectives suggest that complementarity between biotechnology, nanotechnology, and sustainability will be essential to implement the use of bioleaching and metal-binding peptides as a viable and competitive alternative in the recovery of lithium and other metals from secondary sources.

## 7. Conclusions

The recovery of lithium and other metals from LIBs and WEEE has become an environmental priority in light of the growing amount of waste generated. Although pyrometallurgical and hydrometallurgical methods exist for large-scale recovery, they have limitations in terms of cost, selectivity, and sustainability. In this context, biohydrometallurgy through bioleaching emerges as a promising alternative, capable of harnessing the metabolic activity of microorganisms to solubilize metals in environmentally friendly conditions.

On the other hand, the development of metal-binding peptides opens up an innovative avenue for the selective recovery of lithium from other cations present in leachates. This strategy offers the possibility of designing highly specific biomolecules, immobilizing them on the cell surface of microorganisms such as E. coli, B. subtilis, and S. cerevisiae, and combining them with biotechnological processes to improve recovery efficiency.

Overall, the integration of bioleaching and biosorption using peptides represents an emerging line of research that could contribute to the transition towards circular, clean, and economically viable processes. However, challenges remain related to microbial optimization, biomolecule stability, and industrial scaling, which will need to be addressed in future research.

## Author Contributions

Conceptualization, G.A.M.-R., D.R.-J., J.A.R.-C. and D.E.Z.-Á.; methodology, G.A.M.-R., P.G.V.-O. and D.E.Z.-Á.; validation, D.R.-J., H.M.-R., N.U.-E. and M.B.-S.; formal analysis, G.A.M.-R., G.F.-R. and D.E.Z.-Á.; investigation, G.A.M.-R., J.A.R.-C. and D.R.-J.; resources, E.R.-A., H.M.-R., P.G.V.-O. and N.U.-E.; writing—original draft preparation, G.A.M.-R. and D.E.Z.-Á.; writing—review and editing, J.A.R.-C. and D.R.-J.; supervision, M.B.-S. and D.E.Z.-Á.; project administration, J.A.R.-C., P.G.V.-O. and D.R.-J.; funding acquisition, G.F.-R., E.R.-A., H.M.-R., N.U.-E. and M.B.-S. All authors have read and agreed to the published version of the manuscript.

## Funding

This research received no external funding.

## Data Availability Statement

This study did not generate any new data.

## Conflicts of Interest

The authors declare no conflicts of interest.

## References

1. Li, X.; Mo, Y.; Qing, W.; Shao, S.; Tang, C.Y.; Li, J. Membrane-Based Technologies for Lithium Recovery from Water Lithium Resources: A Review. J. Memb. Sci. 2019, 591, 117317. [Google Scholar] [CrossRef]
2. Choubey, P.K.; Kim, M.S.; Srivastava, R.R.; Lee, J.C.; Lee, J.Y. Advance Review on the Exploitation of the Prominent Energy-Storage Element: Lithium. Part I: From Mineral and Brine Resources. Miner. Eng. 2016, 89, 119–137. [Google Scholar] [CrossRef]
3. Roy, J.J.; Madhavi, S.; Cao, B. Metal Extraction from Spent Lithium-Ion Batteries (LIBs) at High Pulp Density by Environmentally Friendly Bioleaching Process. J. Clean. Prod. 2021, 280, 124242. [Google Scholar] [CrossRef]
4. Selvamani, V.; Jeong, J.; Maruthamuthu, M.K.; Arulsamy, K.; Na, J.G.; Hong, S.H. Construction of the Lithium Binding Peptide Displayed Recombinant Escherichia coli for the Specific Lithium Removal from Various Metal Polluted Wastewater. J. Environ. Chem. Eng. 2023, 11, 109029. [Google Scholar] [CrossRef]
5. Etude, M.C.; Ikeuba, A.I.; Njoku, C.N.; Yakubu, E.; Uzoma, H.C.; Mgbemere, C.E.; Udunwa, D.I. Recycling Lithium-Ion Batteries: A Review of Current Status and Future Directions. Sustain. Chem. One World 2024, 4, 100027. [Google Scholar] [CrossRef]
6. Moazzam, P.; Boroumand, Y.; Rabiei, P.; Baghbaderani, S.S.; Mokarian, P.; Mohagheghian, F.; Mohammed, L.J.; Razmjou, A. Lithium Bioleaching: An Emerging Approach for the Recovery of Li from Spent Lithium Ion Batteries. Chemosphere 2021, 277, 130196. [Google Scholar] [CrossRef] [PubMed]
7. Boxall, N.J.; Cheng, K.Y.; Bruckard, W.; Kaksonen, A.H. Application of Indirect Non-Contact Bioleaching for Extracting Metals from Waste Lithium-Ion Batteries. J. Hazard Mater. 2018, 360, 504–511. [Google Scholar] [CrossRef]
8. Biswal, B.K.; Balasubramanian, R. Recovery of Valuable Metals from Spent Lithium-Ion Batteries Using Microbial Agents for Bioleaching: A Review. Front. Microbiol. 2023, 14, 1197081. [Google Scholar] [CrossRef]
9. Gavrilescu, M. Microbial Recovery of Critical Metals from Secondary Sources. Bioresour. Technol. 2022, 344, 126208. [Google Scholar] [CrossRef] [PubMed]
10. Maruthamuthu, M.K.; Selvamani, V.; Nadarajan, S.P.; Yun, H.; Oh, Y.K.; Eom, G.T.; Hong, S.H. Manganese and Cobalt Recovery by Surface Display of Metal Binding Peptide on Various Loops of OmpC in Escherichia coli. J. Ind. Microbiol. Biotechnol. 2018, 45, 31–41. [Google Scholar] [CrossRef]
11. Xu, J.; Sun, J.; Wang, Y.; Sheng, J.; Wang, F.; Sun, M. Application of Iron Magnetic Nanoparticles in Protein Immobilization. Molecules 2014, 19, 11465–11486. [Google Scholar] [CrossRef]
12. Jeong, J.; Selvamani, V.; Maruthamuthu, M.K.; Arulsamy, K.; Hong, S.H. Application of the Surface Engineered Recombinant Escherichia coli to the Industrial Battery Waste Solution for Lithium Recovery. J. Ind. Microbiol. Biotechnol. 2024, 51, kuae012. [Google Scholar] [CrossRef]
13. Secretaría de Economía. Dirección General de Desarrollo Minero Perfil Del Mercado Del Litio 2021. Available online: https://www.gob.mx/cms/uploads/attachment/file/692315/15._Perfil_Litio_2021__T_.pdf(accessed on 20 November 2025).
14. Heydarian, A.; Mousavi, S.M.; Vakilchap, F.; Baniasadi, M. Application of a Mixed Culture of Adapted Acidophilic Bacteria in Two-Step Bioleaching of Spent Lithium-Ion Laptop Batteries. J. Power Sources 2018, 378, 19–30. [Google Scholar] [CrossRef]
15. Biswal, B.K.; Jadhav, U.U.; Madhaiyan, M.; Ji, L.; Yang, E.H.; Cao, B. Biological Leaching and Chemical Precipitation Methods for Recovery of Co and Li from Spent Lithium-Ion Batteries. ACS Sustain. Chem. Eng. 2018, 6, 12343–12352. [Google Scholar] [CrossRef]
16. Domingues, A.M.; de Souza, R.G. Review of Life Cycle Assessment on Lithium-Ion Batteries (LIBs) Recycling. Next Sustain. 2024, 3, 100032. [Google Scholar] [CrossRef]
17. Aaltonen, M.; Peng, C.; Wilson, B.P.; Lundström, M. Leaching of Metals from Spent Lithium-Ion Batteries. Recycling 2017, 2, 20. [Google Scholar] [CrossRef]
18. Roy, J.J.; Cao, B.; Madhavi, S. A Review on the Recycling of Spent Lithium-Ion Batteries (LIBs) by the Bioleaching Approach. Chemosphere 2021, 282, 130944. [Google Scholar] [CrossRef]
19. Horeh, N.B.; Mousavi, S.M.; Shojaosadati, S.A. Bioleaching of Valuable Metals from Spent Lithium-Ion Mobile Phone Batteries Using Aspergillus niger. J. Power Sources 2016, 320, 257–266. [Google Scholar] [CrossRef]
20. Zhao, Y.; Pohl, O.; Bhatt, A.I.; Collis, G.E.; Mahon, P.J.; Rüther, T.; Hollenkamp, A.F. A Review on Battery Market Trends, Second-Life Reuse, and Recycling. Sustain. Chem. 2021, 2, 167–205. [Google Scholar] [CrossRef]
21. Desmarais, M.; Pirade, F.; Zhang, J.; Rene, E.R. Biohydrometallurgical Processes for the Recovery of Precious and Base Metals from Waste Electrical and Electronic Equipments: Current Trends and Perspectives. Bioresour. Technol. Rep. 2020, 11, 100526. [Google Scholar] [CrossRef]
22. Hoque, M.E.; Philip, O.J. Biotechnological Recovery of Heavy Metals from Secondary Sources—An Overview. Mater. Sci. Eng. C 2011, 31, 57–66. [Google Scholar] [CrossRef]
23. Priya, A.; Hait, S. Comparative Assessment of Metallurgical Recovery of Metals from Electronic Waste with Special Emphasis on Bioleaching. Environ. Sci. Pollut. Res. 2017, 24, 6989–7008. [Google Scholar] [CrossRef] [PubMed]
24. Brown, R.M.; Struhs, E.; Mirkouei, A.; Reed, D. A Novel Continuous Ultrasound-Assisted Leaching Process for Rare Earth Element Extraction: Environmental and Economic Assessment. Sustain. Chem. 2025, 6, 33. [Google Scholar] [CrossRef]
25. Naseri, T.; Bahaloo-Horeh, N.; Mousavi, S.M. Environmentally Friendly Recovery of Valuable Metals from Spent Coin Cells through Two-Step Bioleaching Using Acidithiobacillus thiooxidans. J. Environ. Manag. 2019, 235, 357–367. [Google Scholar] [CrossRef] [PubMed]
26. Naseri, T.; Bahaloo-Horeh, N.; Mousavi, S.M. Bacterial Leaching as a Green Approach for Typical Metals Recovery from End-of-Life Coin Cells Batteries. J. Clean. Prod. 2019, 220, 483–492. [Google Scholar] [CrossRef]
27. Jegan Roy, J.; Srinivasan, M.; Cao, B. Bioleaching as an Eco-Friendly Approach for Metal Recovery from Spent NMC-Based Lithium-Ion Batteries at a High Pulp Density. ACS Sustain. Chem. Eng. 2021, 9, 3060–3069. [Google Scholar] [CrossRef]
28. Huang, T.; Liu, L.; Zhang, S. Recovery of Cobalt, Lithium, and Manganese from the Cathode Active Materials of Spent Lithium-Ion Batteries in a Bio-Electro-Hydrometallurgical Process. Hydrometallurgy 2019, 188, 101–111. [Google Scholar] [CrossRef]
29. Wu, W.; Liu, X.; Zhang, X.; Li, X.; Qiu, Y.; Zhu, M.; Tan, W. Mechanism Underlying the Bioleaching Process of LiCoO2 by Sulfur-Oxidizing and Iron-Oxidizing Bacteria. J. Biosci. Bioeng. 2019, 128, 344–354. [Google Scholar] [CrossRef]
30. Lobos, A. Bioleaching Potential of Filamentous Fungi to Mobilize Lithium and Cobalt from Spent Rechargeable Li-Ion Batteries; University of South Florida: Tampa, FL, USA, 2017. [Google Scholar]
31. Hartono, M.; Astrayudha, M.A.; Petrus, H.T.B.M.; Budhijanto, W.; Sulistyo, H. Lithium Recovery of Spent Lithium-Ion Battery Using Bioleaching from Local Sources Microorganism. Rasayan J. Chem. 2017, 10, 897–903. [Google Scholar] [CrossRef]
32. Alipanah, M.; Jin, H.; Reed, D.W.; Thompson, V.S.; Fujita, Y. Sustainable Bioleaching of Lithium-Ion Batteries for Critical Materials Recovery. J. Clean. Prod. 2023, 382, 135274. [Google Scholar] [CrossRef]
33. Lalropuia, L.; Kucera, J.; Rassy, W.Y.; Pakostova, E.; Schild, D.; Mandl, M.; Kremser, K.; Guebitz, G.M. Metal Recovery from Spent Lithium-Ion Batteries via Two-Step Bioleaching Using Adapted Chemolithotrophs from an Acidic Mine Pit Lake. Front. Microbiol. 2024, 15, 1347072. [Google Scholar] [CrossRef] [PubMed]
34. Naseri, T.; Mousavi, S.M. Improvement of Li and Mn Bioleaching from Spent Lithium-Ion Batteries, Using Step-Wise Addition of Biogenic Sulfuric Acid by Acidithiobacillus thiooxidans. Heliyon 2024, 10, e37447. [Google Scholar] [CrossRef]
35. Xin, Y.; Guo, X.; Chen, S.; Wang, J.; Wu, F.; Xin, B. Bioleaching of Valuable Metals Li, Co, Ni and Mn from Spent Electric Vehicle Li-Ion Batteries for the Purpose of Recovery. J. Clean. Prod. 2016, 116, 249–258. [Google Scholar] [CrossRef]
36. Lim, J.; Jang, Y.; Lee, J.; Lee, C.; Jbari, O.; Kwon, K.; Chung, E. Hydrometallurgical Process of Spent Lithium-Ion Battery Recycling Part. 2 Recovery of Valuable Metals from the Cathode Active Material Leachates: Review and Cost Analysis. Hydrometallurgy 2025, 236, 106516. [Google Scholar] [CrossRef]
37. Nnaji, N.D.; Onyeaka, H.; Miri, T.; Ugwa, C. Bioaccumulation for Heavy Metal Removal: A Review. SN Appl. Sci. 2023, 5, 125. [Google Scholar] [CrossRef]
38. Sieber, A.; Spiess, S.; Rassy, W.Y.; Schild, D.; Rieß, T.; Singh, S.; Jain, R.; Schönberger, N.; Lederer, F.; Kremser, K.; et al. Fundamentals of Bio-Based Technologies for Selective Metal Recovery from Bio-Leachates and Liquid Waste Streams. Front. Bioeng. Biotechnol. 2024, 12, 1528992. [Google Scholar] [CrossRef]
39. Diep, P.; Mahadevan, R.; Yakunin, A.F. Heavy Metal Removal by Bioaccumulation Using Genetically Engineered Microorganisms. Front. Bioeng. Biotechnol. 2018, 6, 157. [Google Scholar] [CrossRef] [PubMed]
40. Sedlakova-Kadukova, J.; Marcincakova, R.; Luptakova, A.; Vojtko, M.; Fujda, M.; Pristas, P. Comparison of Three Different Bioleaching Systems for Li Recovery from Lepidolite. Sci. Rep. 2020, 10, 14594. [Google Scholar] [CrossRef] [PubMed]
41. Tsuruta, T. Removal and Recovery of Lithium Using Various Microorganisms. J. Biosci. Bioeng. 2005, 100, 562–566. [Google Scholar] [CrossRef]
42. Zolgharnei, H.; Karami, K.; Mazaheri, A.M.; Dadolahi, S.A. Investigation of Heavy Metals Biosorption on Pseudomonas aeruginosa Strain MCCB 102 Isolated from the Persian Gulf. Asian J. Biotechnol. 2010, 2, 99–109. [Google Scholar] [CrossRef][Green Version]
43. Arifiyanto, A.; Apriyanti, F.D.; Purwaningsih, P.; Kalqutny, S.H.; Agustina, D.; Surtiningsih, T.; Shovitri, M.; Zulaika, E. Lead (Pb) Bioaccumulation; Genera Bacillus Isolate S1 and SS19 as a Case Study. In Proceedings of the International Biology Conference 2016: Biodiversity and Biotechnology for Human Welfare, Surabaya, Indonesia, 15 October 2016; p. 020003. [Google Scholar]
44. Aslam, F.; Yasmin, A.; Sohail, S. Bioaccumulation of Lead, Chromium, and Nickel by Bacteria from Three Different Genera Isolated from Industrial Effluent. Int. Microbiol. 2020, 23, 253–261. [Google Scholar] [CrossRef] [PubMed]
45. Shamim, S. Biosorption of Heavy Metals. In Biosorption; InTech: London, UK, 2018. [Google Scholar]
46. Mahmoodi, A.; Farinas, E.T. Applications of Bacillus subtilis Protein Display for Medicine, Catalysis, Environmental Remediation, and Protein Engineering. Microorganisms 2024, 12, 97. [Google Scholar] [CrossRef] [PubMed]
47. Valenzuela-García, L.I.; Alarcón-Herrera, M.T.; Ayala-García, V.M.; Barraza-Salas, M.; Salas-Pacheco, J.M.; Díaz-Valles, J.F.; Pedraza-Reyes, M. Design of a Whole-Cell Biosensor Based on Bacillus subtilis Spores and the Green Fluorescent Protein to Monitor Arsenic. Microbiol. Spectr. 2023, 11, e0043223. [Google Scholar] [CrossRef]
48. Hinc, K.; Ghandili, S.; Karbalaee, G.; Shali, A.; Noghabi, K.A.; Ricca, E.; Ahmadian, G. Efficient Binding of Nickel Ions to Recombinant Bacillus subtilis Spores. Res. Microbiol. 2010, 161, 757–764. [Google Scholar] [CrossRef] [PubMed]
49. Guoyan, Z.; Yingfeng, A.; Zabed, H.M.; Qi, G.; Yang, M.; Jiao, Y.; Li, W.; Wenjing, S.; Xianghui, Q. Bacillus subtilis Spore Surface Display Technology: A Review of Its Development and Applications. J. Microbiol. Biotechnol. 2019, 29, 179–190. [Google Scholar] [CrossRef]
50. Dong, W.; Li, S.; Camilleri, E.; Korza, G.; Yankova, M.; King, S.M.; Setlow, P. Accumulation and Release of Rare Earth Ions by Spores of Bacillus Species and the Location of These Ions in Spores. Appl. Environ. Microbiol. 2019, 85, e00956-19. [Google Scholar] [CrossRef]
51. Wei, Q.; Yan, J.; Chen, Y.; Zhang, L.; Wu, X.; Shang, S.; Ma, S.; Xia, T.; Xue, S.; Zhang, H. Cell Surface Display of MerR on Saccharomyces cerevisiae for Biosorption of Mercury. Mol. Biotechnol. 2018, 60, 12–20. [Google Scholar] [CrossRef] [PubMed]
52. Lozančić, M.; Žunar, B.; Hrestak, D.; Lopandić, K.; Teparić, R.; Mrša, V. Systematic Comparison of Cell Wall-Related Proteins of Different Yeasts. J. Fungi 2021, 7, 128. [Google Scholar] [CrossRef]
53. Zhang, C.; Chen, H.; Zhu, Y.; Zhang, Y.; Li, X.; Wang, F. Saccharomyces cerevisiae Cell Surface Display Technology: Strategies for Improvement and Applications. Front. Bioeng. Biotechnol. 2022, 10, 1056804. [Google Scholar] [CrossRef]
54. Wei, Q.; Zhang, H.; Guo, D.; Ma, S. Cell Surface Display of Four Types of Solanum nigrum Metallothionein on Saccharomyces cerevisiae for Biosorption of Cadmium. J. Microbiol. Biotechnol. 2016, 26, 846–853. [Google Scholar] [CrossRef]
55. Beech, I.B.; Sunner, J.A. Sulphate-Reducing Bacteria and Their Role in Corrosion of Ferrous Materials. In Sulphate-Reducing Bacteria; Cambridge University Press: Cambridge, UK, 2007; pp. 459–482. [Google Scholar] [CrossRef]
56. Sethurajan, M.; Gaydardzhiev, S. Bioprocessing of Spent Lithium Ion Batteries for Critical Metals Recovery—A Review. Resour. Conserv. Recycl. 2021, 165, 105225. [Google Scholar] [CrossRef]
57. Calvert, G.; Kaksonen, A.; Cheng, K.; Van Yken, J.; Chang, B.; Boxall, N. Recovery of Metals from Waste Lithium Ion Battery Leachates Using Biogenic Hydrogen Sulfide. Minerals 2019, 9, 563. [Google Scholar] [CrossRef]
58. Van Yken, J.; Boxall, N.J.; Cheng, K.Y.; Nikoloski, A.N.; Moheimani, N.R.; Kaksonen, A.H. Base Metals Recovery from Waste Printed Circuit Board Leachate Using Biogenic Hydrogen Sulfide Gas. Hydrometallurgy 2024, 228, 106341. [Google Scholar] [CrossRef]
59. Dong, Y.; Gao, Z.; Di, J.; Wang, D.; Yang, Z.; Guo, X.; Zhu, X. Study on the Effectiveness of Sulfate-Reducing Bacteria to Remove Pb(II) and Zn(II) in Tailings and Acid Mine Drainage. Front. Microbiol. 2024, 15, 1352430. [Google Scholar] [CrossRef]
60. Zhu, B.; Chen, Y.; Wei, N. Engineering Biocatalytic and Biosorptive Materials for Environmental Applications. Trends Biotechnol. 2019, 37, 661–676. [Google Scholar] [CrossRef]
61. Ruta, L.L.; Lin, Y.-F.; Kissen, R.; Nicolau, I.; Neagoe, A.D.; Ghenea, S.; Bones, A.M.; Farcasanu, I.C. Anchoring Plant Metallothioneins to the Inner Face of the Plasma Membrane of Saccharomyces Cerevisiae Cells Leads to Heavy Metal Accumulation. PLoS ONE 2017, 12, e0178393. [Google Scholar] [CrossRef]
62. Deng, X.; He, J.; He, N. Comparative Study on Ni2+-Affinity Transport of Nickel/Cobalt Permeases (NiCoTs) and the Potential of Recombinant Escherichia coli for Ni2+ Bioaccumulation. Bioresour. Technol. 2013, 130, 69–74. [Google Scholar] [CrossRef] [PubMed]
63. Li, H.; Cong, Y.; Lin, J.; Chang, Y. Enhanced Tolerance and Accumulation of Heavy Metal Ions by Engineered Escherichia coli Expressing Pyrus calleryana Phytochelatin Synthase. J. Basic. Microbiol. 2015, 55, 398–405. [Google Scholar] [CrossRef] [PubMed]
64. Hui, C.-Y.; Guo, Y.; Yang, X.-Q.; Zhang, W.; Huang, X.-Q. Surface Display of Metal Binding Domain Derived from PbrR on Escherichia coli Specifically Increases Lead(II) Adsorption. Biotechnol. Lett. 2018, 40, 837–845. [Google Scholar] [CrossRef]
65. Tang, X.; Zeng, G.; Fan, C.; Zhou, M.; Tang, L.; Zhu, J.; Wan, J.; Huang, D.; Chen, M.; Xu, P.; et al. Chromosomal Expression of CadR on Pseudomonas aeruginosa for the Removal of Cd(II) from Aqueous Solutions. Sci. Total Environ. 2018, 636, 1355–1361. [Google Scholar] [CrossRef]
66. Selvamani, V.; Jeong, J.; Maruthamuthu, M.K.; Arulsamy, K.; Na, J.-G.; Hong, S.H. Adsorption of Lithium on Cell Surface as Nanoparticles through Lithium Binding Peptide Display in Recombinant Escherichia coli. Biotechnol. Bioprocess. Eng. 2023, 28, 255–262. [Google Scholar] [CrossRef]
67. Bhargawa, B.; Hong, S.H.; Yoo, I.K. Adsorptive Lithium Recovery by Magnetic Beads Harboring Lithium-Binding Peptide. Desalination 2024, 577, 117412. [Google Scholar] [CrossRef]

Figure 1. Mass percentage of the main components of a Li-ion battery.

Figure 1. Mass percentage of the main components of a Li-ion battery.

Figure 2. Methods for bioleaching metals from lithium-ion battery powder. (a) One step; (b) two step; (c) spent medium.

Figure 2. Methods for bioleaching metals from lithium-ion battery powder. (a) One step; (b) two step; (c) spent medium.

Figure 3. Bioleaching mechanisms. (a) Direct mechanisms. Cells adhere to the material through extracellular polymeric substances, and oxidation of sulfides and reduction of metals take place. (b) Indirect mechanisms. Microorganisms do not come into contact with the material, and oxidation and reduction processes occur.

Figure 3. Bioleaching mechanisms. (a) Direct mechanisms. Cells adhere to the material through extracellular polymeric substances, and oxidation of sulfides and reduction of metals take place. (b) Indirect mechanisms. Microorganisms do not come into contact with the material, and oxidation and reduction processes occur.

Figure 4. (a) Bioaccumulation takes place in two steps; in the first step, metals are trapped on the cell surface, and in the second step, they are transported inside the cell by functional groups and trapped by ligands. (b) Biosorption is mediated by the negative charge of the cell wall due to the presence of teichoic acid, phospholipids, and lipopolysaccharides that adsorb metals on the surface.

Figure 4. (a) Bioaccumulation takes place in two steps; in the first step, metals are trapped on the cell surface, and in the second step, they are transported inside the cell by functional groups and trapped by ligands. (b) Biosorption is mediated by the negative charge of the cell wall due to the presence of teichoic acid, phospholipids, and lipopolysaccharides that adsorb metals on the surface.

Figure 5. Strategies for displaying proteins on (a) the cell surface of Escherichia coli, (b) the spore of Bacillus subtilis, and (c) the cell wall surface of Saccharomyces cerevisiae.

Figure 5. Strategies for displaying proteins on (a) the cell surface of Escherichia coli, (b) the spore of Bacillus subtilis, and (c) the cell wall surface of Saccharomyces cerevisiae.

Table 1. Bioleaching of secondary sources of lithium and other metals, mechanisms and conditions.

Table 1. Bioleaching of secondary sources of lithium and other metals, mechanisms and conditions.

| Material | Microorganism | Bioleaching Method | Results | References |
| --- | --- | --- | --- | --- |
| LIBs | A. niger | One step, two step, spent-medium | With spent-medium a maximum recovery efficiency of Cu 100%, Li 95%, Mn 70%, Al 65%, Co 45%, and Ni 38% | [19] |
| LIBs | Native bacteria | One step | Optimal Li recovery of 62.83% | [31] |
| LIBs | A. niger MM1 and SG1, A. thiooxidans 80191 | One step, spent-medium | Highest recovery rates for Co 82% and Li 100% using the MM1 strain with spent-medium | [15] |
| LIBs | A. ferrooxidans, A. thiooxidans | Spent-medium | Co 53%, Li 60% | [7] |
| LIBs | A. ferrooxidans, A. thiooxidans | Two step | Co 50.4%, Li 99.2% | [14] |
| LIBs | Sulfur-oxidizing bacteria | Two step | Co 91.45%, Li 93.64 | [28] |
| Waste coin batteries | A. ferrooxidans | Two step | Co 88%, Li 100% | [26] |
| Waste coin batteries | A. thiooxidans | Two step | Co 60%, Li 99% | [25] |
| LiCO2 batteries | Sulfur-oxidizing and iron-oxidizing bacteria | One step | Pyrite addition: Co 94.2%, Li 91.4% | [29] |
| NMC LIBs | A. ferrooxidans | Two step | Co 82%, Li 89% | [27] |
| LIBs | A. ferrooxidans | Two step | 100 g/L pulp density with replenished cycles: Co 94%, Li 60% | [3] |
| LIBs | Gluconobacter oxydans | Spent-medium | Co 71–86%, Li 100%, Mn 100%, Ni 57–84% | [32] |
| NMC LIBs | Consortium of adapted acidophiles | Two step | 10 g/L pulp density: Co 2.92 g/L, Li 0.43 g/L | [33] |
| LIBs | A. thiooxidans | Spent-medium + addition of biogenic acid | Li 93%, Mn 15% | [34] |

Table 2. Studies of engineered microorganisms expressing metal-binding peptides or proteins.

Table 2. Studies of engineered microorganisms expressing metal-binding peptides or proteins.

| Donor Organism | Host | Peptide/Protein | Target Metal | Reference |
| --- | --- | --- | --- | --- |
| Peas and Helicobacter pylori | E. coli | MTs and NiCoT transporter protein | Ni | [62] |
| Pyrus calleryana | E. coli | PcPCS1 gene for phytochelatin synthase | Cd, Cu, Hg | [63] |
| Arabidopsis thaliana and Noccaea caerulescens | Saccharomyces cerevisiae | MTs | Cu, Zn, Mn, Ni, Co, Cd | [61] |
| – | E. coli | Lead (Pb) binding domain | Pb | [64] |
| – | Pseudomonas aeruginosa | Cadmium-induced regulatory protein CadR | Cd | [65] |

| Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content. |
| --- |

© 2025 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license.

## Share and Cite

MDPI and ACS Style

Martinez-Rodriguez, G.A.; Rojas-Contreras, J.A.; Vázquez-Ortega, P.G.; Reyes-Jáquez, D.; Medrano-Roldán, H.; Urtiz-Estrada, N.; Barraza-Salas, M.; Fierros-Romero, G.; Rodríguez-Andrade, E.; Zazueta-Álvarez, D.E. Biotechnological Strategies for the Recovery of Lithium and Other Metals from a Secondary Source: The Role of Microorganisms and Metal-Binding Peptides. Recycling 2026, 11, 4. https://doi.org/10.3390/recycling11010004

AMA Style

Martinez-Rodriguez GA, Rojas-Contreras JA, Vázquez-Ortega PG, Reyes-Jáquez D, Medrano-Roldán H, Urtiz-Estrada N, Barraza-Salas M, Fierros-Romero G, Rodríguez-Andrade E, Zazueta-Álvarez DE. Biotechnological Strategies for the Recovery of Lithium and Other Metals from a Secondary Source: The Role of Microorganisms and Metal-Binding Peptides. Recycling. 2026; 11(1):4. https://doi.org/10.3390/recycling11010004

Chicago/Turabian Style

Martinez-Rodriguez, Gloria Abigail, Juan Antonio Rojas-Contreras, Perla Guadalupe Vázquez-Ortega, Damián Reyes-Jáquez, Hiram Medrano-Roldán, Norma Urtiz-Estrada, Marcelo Barraza-Salas, Grisel Fierros-Romero, Ernesto Rodríguez-Andrade, and David Enrique Zazueta-Álvarez. 2026. "Biotechnological Strategies for the Recovery of Lithium and Other Metals from a Secondary Source: The Role of Microorganisms and Metal-Binding Peptides" Recycling 11, no. 1: 4. https://doi.org/10.3390/recycling11010004

APA Style

Martinez-Rodriguez, G. A., Rojas-Contreras, J. A., Vázquez-Ortega, P. G., Reyes-Jáquez, D., Medrano-Roldán, H., Urtiz-Estrada, N., Barraza-Salas, M., Fierros-Romero, G., Rodríguez-Andrade, E., & Zazueta-Álvarez, D. E. (2026). Biotechnological Strategies for the Recovery of Lithium and Other Metals from a Secondary Source: The Role of Microorganisms and Metal-Binding Peptides. Recycling, 11(1), 4. https://doi.org/10.3390/recycling11010004

## Article Metrics

No

No

### Article Access Statistics

For more information on the journal statistics, click here.

Multiple requests from the same IP address are counted as one view.

Zoom | Orient | As Lines | As Sticks | As Cartoon | As Surface | Previous Scene | Next Scene

Recycling, EISSN 2313-4321, Published by MDPI

RSS Content Alert

### Further Information

### Guidelines

For Authors For Reviewers For Editors For Librarians For Publishers For Societies For Conference Organizers

### MDPI Initiatives

### Follow MDPI

Subscribe to receive issue release notifications and newsletters from MDPI journals

Accounting and Auditing Acoustics Acta Microbiologica Hellenica Actuators Addiction & Prevention Adhesives Administrative Sciences Adolescents Advances in Respiratory Medicine Aerobiology Aerospace Agriculture AgriEngineering Agrochemicals Agronomy AI AI and Precision Agriculture AI Chemistry AI for Engineering AI in Education AI in Medicine AI Materials AI Sensors Air Algorithms Allergies Alloys Analog Analytica Analytics Anatomia Anesthesia Research Animals Antibiotics Antibodies Antioxidants Applied Biosciences Applied Mechanics Applied Microbiology Applied Nano Applied Sciences Applied System Innovation AppliedChem AppliedMath AppliedPhys Aquaculture Journal Archaeological Studies Architecture Arthropoda Arts Astronautics Astronomy Atmosphere Atoms Audiology Research Automation Axioms Bacteria Batteries Behavioral Sciences Beverages Big Data and Cognitive Computing BioChem Bioengineering Biologics Biology Biology and Life Sciences Forum Biomass Biomechanics BioMed Biomedicines BioMedInformatics Biomimetics Biomolecules Biophysica Bioresources and Bioproducts Biosensors Biosphere BioTech Birds Blockchains Brain Sciences Breast Cancer Research and Care Buildings Businesses C Cancers Cardiogenetics Cardiovascular Medicine Catalysts Cells Ceramics Challenges ChemEngineering Chemistry Chemistry Proceedings Chemosensors Children Chips CivilEng Clean Technologies Climate Clinical and Translational Neuroscience Clinical Bioenergetics Clinics and Practice Clocks & Sleep Coasts Coatings Colloids and Interfaces Colorants Commodities Complexities Complications Compounds Computation Computer Sciences & Mathematics Forum Computers Condensed Matter Conservation Construction Materials Corrosion and Materials Degradation Cosmetics COVID Crafts Craniomaxillofacial Trauma & Reconstruction Crops Cryo Cryptography Crystals Culture Current Issues in Molecular Biology Current Oncology Dairy Data Dentistry Journal Dermato Dermatopathology Designs Diabetology Diagnostics Dietetics Digital Digital Health and Innovation Disabilities Diseases Diversity DNA Drones Drugs and Drug Candidates Dynamics Earth Ecologies Econometrics Economies Education Sciences Electricity Electrochem Electronic Materials Electronics Emergency Care and Medicine Encyclopedia Endocrines Energies Energy Storage and Applications Eng Engineering Proceedings Entropic and Disordered Matter Entropy Environmental and Earth Sciences Proceedings Environmental Remediation Environments Epidemiologia Epigenomes European Burn Journal European Journal of Investigation in Health, Psychology and Education Family Sciences Fermentation Fibers FinTech Fire Fishes Fluids Foods Forecasting Forensic Sciences Forests Fossil Studies Foundations Fractal and Fractional Freshwater Fuels Future Future Collections, Libraries, Archives, and Museums Future Internet Future Pharmacology Future Transportation Galaxies Games Gases Gastroenterology Insights Gastrointestinal Disorders Gastronomy Gels Genealogy Genes Geographies GeoHazards Geomatics Geometry Geosciences Geotechnics Geriatrics Germs Glacies Gout, Urate, and Crystal Deposition Disease Grasses Green Green Health Hardware Healthcare Hearts Hemato Hematology Reports Heritage Histories Horticulturae Hospitals Humanities Humans Hydrobiology Hydrogen Hydrology Hydropower Hygiene Immuno Industries Infectious Disease Reports Inflammation Journal Informatics Information Infrastructures Inorganics Insects Instruments Intelligent Infrastructure and Construction International Journal of Cognitive Sciences International Journal of Environmental Medicine International Journal of Environmental Research and Public Health International Journal of Financial Studies International Journal of Medical Devices International Journal of Molecular Sciences International Journal of Neonatal Screening International Journal of Orofacial Myology and Myofunctional Therapy International Journal of Plant Biology International Journal of Thermofluid Science and Technology International Journal of Topology International Journal of Translational Medicine International Journal of Turbomachinery, Propulsion and Power International Medical Education Inventions IoT ISPRS International Journal of Geo-Information J Journal of Aesthetic Medicine Journal of Ageing and Longevity Journal of CardioRenal Medicine Journal of Cardiovascular Development and Disease Journal of Clinical & Translational Ophthalmology Journal of Clinical Medicine Journal of Composites Science Journal of Cybersecurity and Privacy Journal of Dementia and Alzheimer's Disease Journal of Developmental Biology Journal of Experimental and Theoretical Analyses Journal of Eye Movement Research Journal of Functional Biomaterials Journal of Functional Morphology and Kinesiology Journal of Fungi Journal of Genome Biotechnology and Genetics Journal of Gerontology and Geriatrics Journal of Imaging Journal of Innovation Journal of Intelligence Journal of Interdisciplinary Research Applied to Medicine Journal of Low Power Electronics and Applications Journal of Manufacturing and Materials Processing Journal of Marine Science and Engineering Journal of Market Access & Health Policy Journal of Mind and Medical Sciences Journal of Molecular Pathology Journal of Nanotheranostics Journal of Nuclear Engineering Journal of Optical Materials Journal of Otorhinolaryngology, Hearing and Balance Medicine Journal of Parks Journal of Personalized Medicine Journal of Pharmaceutical and BioTech Industry Journal of Phytomedicine Journal of Respiration Journal of Risk and Financial Management Journal of Sensor and Actuator Networks Journal of Superintelligence Journal of the American Podiatric Medical Association Journal of the Oman Medical Association Journal of Theoretical and Applied Electronic Commerce Research Journal of Vascular Diseases Journal of Xenobiotics Journal of Zoological and Botanical Gardens Journalism and Media Kidney and Dialysis Kinases and Phosphatases Knowledge LabMed Laboratories Land Languages Laws Life Lights Limnological Review Lipidology Liquids Literature Livers Logics Logistics Low-Altitude Economy Lubricants Lymphatics Machine Learning and Knowledge Extraction Machines Macromol Magnetism Magnetochemistry Marine Drugs Materials Materials Proceedings Mathematical and Computational Applications Mathematics Medical Sciences Medical Sciences Forum Medicina Medicines Membranes Merits Metabolites Metals Meteorology Methane Methods and Protocols Metrics Metrology Micro Microbiology Research Microelectronics Micromachines Microorganisms Microplastics Microwave Minerals Mining Modelling Modern Mathematical Physics Molbank Molecules Multimedia Multimodal Technologies and Interaction Muscles Nanoenergy Advances Nanomanufacturing Nanomaterials NDT Network Neuroglia Neuroimaging Neurology International NeuroSci Nitrogen Non-Coding RNA Nursing Reports Nutraceuticals Nutrients Obesities Occupational Health Oceans Onco Optics Oral Organics Organoids Osteology Oxygen Pandemics Parasitologia Particles Pathogens Pathophysiology Peace Studies Pediatric Reports Pets Pharmaceuticals Pharmaceutics Pharmacoepidemiology Pharmacy Philosophies Photochem Photonics Photovoltaics Phycology Physchem Physical Sciences Forum Physics Physiologia Plants Plasma Platforms Pollutants Polymers Polysaccharides Populations Poultry Powders Precision Oncology Primary and Hospital Care Proceedings Processes Prosthesis Proteomes Psychiatry International Psychoactives Psychology International Publications Purification Quantum Beam Science Quantum Reports Quaternary Radiation Reactions Real Estate Receptors Recycling Regional Science and Environmental Economics Religions Remote Sensing Reports Reproductive Medicine Resources Rheumato Risks Robotics Romanian Journal of Preventive Medicine Ruminants Safety Sci Scientia Pharmaceutica Sclerosis Seeds Semiconductors and Heterogeneous Integration Sensors Separations Sexes Signals Sinusitis Smart Cities Smart Fisheries Social Sciences Société Internationale d’Urologie Journal Societies Software Soil Systems Solar Solids Spectroscopy Journal Sports Standards Stats Stratigraphy and Sedimentology Stresses Surfaces Surgeries Surgical Techniques Development Sustainability Sustainable Chemistry Swiss Archives of Neurology, Psychiatry and Psychotherapy Symmetry SynBio Systems Targets Taxonomy Technologies Telecom Textiles Thalassemia Reports Theoretical and Applied Ergonomics Therapeutics Thermo Time and Space Tomography Tourism and Hospitality Toxics Toxins Transplantology Trauma Care Trends in Higher Education Trends in Public Health Tropical Medicine and Infectious Disease Universe Urban Science Uro Vaccines Vehicles Venereology Veterinary Sciences Vibration Virtual Worlds Viruses Vision Waste Water Welding Wild Wind Women World World Electric Vehicle Journal Youth Zoonotic Diseases

Select options

- Accounting and Auditing
- Acoustics
- Acta Microbiologica Hellenica
- Actuators
- Addiction & Prevention
- Adhesives
- Administrative Sciences
- Adolescents
- Advances in Respiratory Medicine
- Aerobiology
- Aerospace
- Agriculture
- AgriEngineering
- Agrochemicals
- Agronomy
- AI
- AI and Precision Agriculture
- AI Chemistry
- AI for Engineering
- AI in Education
- AI in Medicine
- AI Materials
- AI Sensors
- Air
- Algorithms
- Allergies
- Alloys
- Analog
- Analytica
- Analytics
- Anatomia
- Anesthesia Research
- Animals
- Antibiotics
- Antibodies
- Antioxidants
- Applied Biosciences
- Applied Mechanics
- Applied Microbiology
- Applied Nano
- Applied Sciences
- Applied System Innovation
- AppliedChem
- AppliedMath
- AppliedPhys
- Aquaculture Journal
- Archaeological Studies
- Architecture
- Arthropoda
- Arts
- Astronautics
- Astronomy
- Atmosphere
- Atoms
- Audiology Research
- Automation
- Axioms
- Bacteria
- Batteries
- Behavioral Sciences
- Beverages
- Big Data and Cognitive Computing
- BioChem
- Bioengineering
- Biologics
- Biology
- Biology and Life Sciences Forum
- Biomass
- Biomechanics
- BioMed
- Biomedicines
- BioMedInformatics
- Biomimetics
- Biomolecules
- Biophysica
- Bioresources and Bioproducts
- Biosensors
- Biosphere
- BioTech
- Birds
- Blockchains
- Brain Sciences
- Breast Cancer Research and Care
- Buildings
- Businesses
- C
- Cancers
- Cardiogenetics
- Cardiovascular Medicine
- Catalysts
- Cells
- Ceramics
- Challenges
- ChemEngineering
- Chemistry
- Chemistry Proceedings
- Chemosensors
- Children
- Chips
- CivilEng
- Clean Technologies
- Climate
- Clinical and Translational Neuroscience
- Clinical Bioenergetics
- Clinics and Practice
- Clocks & Sleep
- Coasts
- Coatings
- Colloids and Interfaces
- Colorants
- Commodities
- Complexities
- Complications
- Compounds
- Computation
- Computer Sciences & Mathematics Forum
- Computers
- Condensed Matter
- Conservation
- Construction Materials
- Corrosion and Materials Degradation
- Cosmetics
- COVID
- Crafts
- Craniomaxillofacial Trauma & Reconstruction
- Crops
- Cryo
- Cryptography
- Crystals
- Culture
- Current Issues in Molecular Biology
- Current Oncology
- Dairy
- Data
- Dentistry Journal
- Dermato
- Dermatopathology
- Designs
- Diabetology
- Diagnostics
- Dietetics
- Digital
- Digital Health and Innovation
- Disabilities
- Diseases
- Diversity
- DNA
- Drones
- Drugs and Drug Candidates
- Dynamics
- Earth
- Ecologies
- Econometrics
- Economies
- Education Sciences
- Electricity
- Electrochem
- Electronic Materials
- Electronics
- Emergency Care and Medicine
- Encyclopedia
- Endocrines
- Energies
- Energy Storage and Applications
- Eng
- Engineering Proceedings
- Entropic and Disordered Matter
- Entropy
- Environmental and Earth Sciences Proceedings
- Environmental Remediation
- Environments
- Epidemiologia
- Epigenomes
- European Burn Journal
- European Journal of Investigation in Health, Psychology and Education
- Family Sciences
- Fermentation
- Fibers
- FinTech
- Fire
- Fishes
- Fluids
- Foods
- Forecasting
- Forensic Sciences
- Forests
- Fossil Studies
- Foundations
- Fractal and Fractional
- Freshwater
- Fuels
- Future
- Future Collections, Libraries, Archives, and Museums
- Future Internet
- Future Pharmacology
- Future Transportation
- Galaxies
- Games
- Gases
- Gastroenterology Insights
- Gastrointestinal Disorders
- Gastronomy
- Gels
- Genealogy
- Genes
- Geographies
- GeoHazards
- Geomatics
- Geometry
- Geosciences
- Geotechnics
- Geriatrics
- Germs
- Glacies
- Gout, Urate, and Crystal Deposition Disease
- Grasses
- Green
- Green Health
- Hardware
- Healthcare
- Hearts
- Hemato
- Hematology Reports
- Heritage
- Histories
- Horticulturae
- Hospitals
- Humanities
- Humans
- Hydrobiology
- Hydrogen
- Hydrology
- Hydropower
- Hygiene
- Immuno
- Industries
- Infectious Disease Reports
- Inflammation Journal
- Informatics
- Information
- Infrastructures
- Inorganics
- Insects
- Instruments
- Intelligent Infrastructure and Construction
- International Journal of Cognitive Sciences
- International Journal of Environmental Medicine
- International Journal of Environmental Research and Public Health
- International Journal of Financial Studies
- International Journal of Medical Devices
- International Journal of Molecular Sciences
- International Journal of Neonatal Screening
- International Journal of Orofacial Myology and Myofunctional Therapy
- International Journal of Plant Biology
- International Journal of Thermofluid Science and Technology
- International Journal of Topology
- International Journal of Translational Medicine
- International Journal of Turbomachinery, Propulsion and Power
- International Medical Education
- Inventions
- IoT
- ISPRS International Journal of Geo-Information
- J
- Journal of Aesthetic Medicine
- Journal of Ageing and Longevity
- Journal of CardioRenal Medicine
- Journal of Cardiovascular Development and Disease
- Journal of Clinical & Translational Ophthalmology
- Journal of Clinical Medicine
- Journal of Composites Science
- Journal of Cybersecurity and Privacy
- Journal of Dementia and Alzheimer's Disease
- Journal of Developmental Biology
- Journal of Experimental and Theoretical Analyses
- Journal of Eye Movement Research
- Journal of Functional Biomaterials
- Journal of Functional Morphology and Kinesiology
- Journal of Fungi
- Journal of Genome Biotechnology and Genetics
- Journal of Gerontology and Geriatrics
- Journal of Imaging
- Journal of Innovation
- Journal of Intelligence
- Journal of Interdisciplinary Research Applied to Medicine
- Journal of Low Power Electronics and Applications
- Journal of Manufacturing and Materials Processing
- Journal of Marine Science and Engineering
- Journal of Market Access & Health Policy
- Journal of Mind and Medical Sciences
- Journal of Molecular Pathology
- Journal of Nanotheranostics
- Journal of Nuclear Engineering
- Journal of Optical Materials
- Journal of Otorhinolaryngology, Hearing and Balance Medicine
- Journal of Parks
- Journal of Personalized Medicine
- Journal of Pharmaceutical and BioTech Industry
- Journal of Phytomedicine
- Journal of Respiration
- Journal of Risk and Financial Management
- Journal of Sensor and Actuator Networks
- Journal of Superintelligence
- Journal of the American Podiatric Medical Association
- Journal of the Oman Medical Association
- Journal of Theoretical and Applied Electronic Commerce Research
- Journal of Vascular Diseases
- Journal of Xenobiotics
- Journal of Zoological and Botanical Gardens
- Journalism and Media
- Kidney and Dialysis
- Kinases and Phosphatases
- Knowledge
- LabMed
- Laboratories
- Land
- Languages
- Laws
- Life
- Lights
- Limnological Review
- Lipidology
- Liquids
- Literature
- Livers
- Logics
- Logistics
- Low-Altitude Economy
- Lubricants
- Lymphatics
- Machine Learning and Knowledge Extraction
- Machines
- Macromol
- Magnetism
- Magnetochemistry
- Marine Drugs
- Materials
- Materials Proceedings
- Mathematical and Computational Applications
- Mathematics
- Medical Sciences
- Medical Sciences Forum
- Medicina
- Medicines
- Membranes
- Merits
- Metabolites
- Metals
- Meteorology
- Methane
- Methods and Protocols
- Metrics
- Metrology
- Micro
- Microbiology Research
- Microelectronics
- Micromachines
- Microorganisms
- Microplastics
- Microwave
- Minerals
- Mining
- Modelling
- Modern Mathematical Physics
- Molbank
- Molecules
- Multimedia
- Multimodal Technologies and Interaction
- Muscles
- Nanoenergy Advances
- Nanomanufacturing
- Nanomaterials
- NDT
- Network
- Neuroglia
- Neuroimaging
- Neurology International
- NeuroSci
- Nitrogen
- Non-Coding RNA
- Nursing Reports
- Nutraceuticals
- Nutrients
- Obesities
- Occupational Health
- Oceans
- Onco
- Optics
- Oral
- Organics
- Organoids
- Osteology
- Oxygen
- Pandemics
- Parasitologia
- Particles
- Pathogens
- Pathophysiology
- Peace Studies
- Pediatric Reports
- Pets
- Pharmaceuticals
- Pharmaceutics
- Pharmacoepidemiology
- Pharmacy
- Philosophies
- Photochem
- Photonics
- Photovoltaics
- Phycology
- Physchem
- Physical Sciences Forum
- Physics
- Physiologia
- Plants
- Plasma
- Platforms
- Pollutants
- Polymers
- Polysaccharides
- Populations
- Poultry
- Powders
- Precision Oncology
- Primary and Hospital Care
- Proceedings
- Processes
- Prosthesis
- Proteomes
- Psychiatry International
- Psychoactives
- Psychology International
- Publications
- Purification
- Quantum Beam Science
- Quantum Reports
- Quaternary
- Radiation
- Reactions
- Real Estate
- Receptors
- Recycling
- Regional Science and Environmental Economics
- Religions
- Remote Sensing
- Reports
- Reproductive Medicine
- Resources
- Rheumato
- Risks
- Robotics
- Romanian Journal of Preventive Medicine
- Ruminants
- Safety
- Sci
- Scientia Pharmaceutica
- Sclerosis
- Seeds
- Semiconductors and Heterogeneous Integration
- Sensors
- Separations
- Sexes
- Signals
- Sinusitis
- Smart Cities
- Smart Fisheries
- Social Sciences
- Société Internationale d’Urologie Journal
- Societies
- Software
- Soil Systems
- Solar
- Solids
- Spectroscopy Journal
- Sports
- Standards
- Stats
- Stratigraphy and Sedimentology
- Stresses
- Surfaces
- Surgeries
- Surgical Techniques Development
- Sustainability
- Sustainable Chemistry
- Swiss Archives of Neurology, Psychiatry and Psychotherapy
- Symmetry
- SynBio
- Systems
- Targets
- Taxonomy
- Technologies
- Telecom
- Textiles
- Thalassemia Reports
- Theoretical and Applied Ergonomics
- Therapeutics
- Thermo
- Time and Space
- Tomography
- Tourism and Hospitality
- Toxics
- Toxins
- Transplantology
- Trauma Care
- Trends in Higher Education
- Trends in Public Health
- Tropical Medicine and Infectious Disease
- Universe
- Urban Science
- Uro
- Vaccines
- Vehicles
- Venereology
- Veterinary Sciences
- Vibration
- Virtual Worlds
- Viruses
- Vision
- Waste
- Water
- Welding
- Wild
- Wind
- Women
- World
- World Electric Vehicle Journal
- Youth
- Zoonotic Diseases

Subscribe

© 1996-2026 MDPI (Basel, Switzerland) unless otherwise stated

Disclaimer

We use cookies on our website to ensure you get the best experience. Read more about our cookies here.

Accept