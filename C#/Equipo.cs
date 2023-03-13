using System;

public class Equipo {
	private String nombre;
	private int id;
	private ScrumMaster scrumMaster;
    private Integrante integrantes;

	public String GetNombre() {
		return this.nombre;
	}
	public void SetNombre(ref String nombre) {
		this.nombre = nombre;
	}
	public int GetId() {
		return this.id;
	}
	public void SetId(ref int id) {
		this.id = id;
	}
	public ScrumMaster GetScrumMaster() {
		return this.scrumMaster;
	}
	public void SetScrumMaster(ref ScrumMaster scrumMaster) {
		this.scrumMaster = scrumMaster;
	}
    public Integrante getIntegrantes() {
		return integrantes;
	}

	public void setIntegrantes(Integrante integrantes) {
		this.integrantes = integrantes;
	}

    public void AddIntegrate(ref Integrante integrante) {
	}
	public Equipo(int id, String nombre, ScrumMaster scrumMaster, Integrante integrantes) {
		this.id = id;
        this.nombre = nombre;
        this.scrumMaster = scrumMaster;
        this.integrantes = integrantes;
	}
    public override String ToString() {
		return base.ToString() + "Id: "+ id.ToString() + "\n" + "Nombre : " + nombre.ToString() +"\n"
        + "Encargado : " + scrumMaster.ToString() +"\n" + "Integrantes : " + integrantes.ToString() +"\n";
	}

}