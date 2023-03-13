using System;

public class ScrumMaster {
	private String nombre;
	private String rolSecundario;

	public String GetNombre() {
		return this.nombre;
	}
	public void SetNombre(ref String nombre) {
		this.nombre = nombre;
	}
	public String GetRolSecundario() {
		return this.rolSecundario;
	}
	public void SetRolSecundario(ref String rolSecundario) {
		this.rolSecundario = rolSecundario;
	}
	public ScrumMaster(ref String nombre, ref String rolSecundario) {
		throw new System.NotImplementedException("Not implemented");
	}

	private Equipo hasA;

}
